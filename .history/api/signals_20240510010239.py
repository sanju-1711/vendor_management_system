from django.db.models.signals import pre_save, post_save
from django.db.models import F, Sum, ExpressionWrapper, Avg, fields
from datetime import timedelta
from django.dispatch import receiver
from .models import *

'''
    Here django signals will be used to calculate real-time when PO related data is modified
'''

@receiver(post_save, sender = Purchase_Order)
def on_time_delivery_rate(sender, instance, **kwargs):
    '''
    here, if in purchase_order model, status changed to completed, 
    then we'll calculate on time delivery rate for those completed orders
    and store it in vendor model.
    '''
    if instance.status == 'Completed' and instance.quality_rating is None:
        total_completed_POs = Purchase_Order.objects.filter(status = 'Completed').count()
        completed_POs_before_delivery = Purchase_Order.objects.filter(
            status = 'Completed',
            delivery_date__lte = F('acknowledgement_date')
        ).count()

        try:
            delivery_rate_on_time = completed_POs_before_delivery / total_completed_POs
            vendor_data = Vendor.objects.get(vendor_code = instance.vendor.vendor_code)
            vendor_data.on_time_delivery_rate = delivery_rate_on_time
            vendor_data.save()
        except ZeroDivisionError as e:
            return e.with_traceback()
        
@receiver(post_save, sender = Purchase_Order)
def quality_rating_avg(sender, instance, **kwargs):
    '''
    here, if in purchase_order model, status changed to completed, and quality_rating is given, 
    then we'll calculate quality rating avg for those completed orders
    and store it in vendor model.
    '''
    if instance.status == 'Completed' and instance.quality_rating is not None:
        get_all_ratings = Purchase_Order.objects.filter(quality_rating__isnull = False, vendor = instance.vendor)
        get_all_ratings_sum = get_all_ratings.aggregate(get_all_ratings_sum = Sum('quality_rating'))['get_all_ratings_sum']
        get_all_ratings_cnt = get_all_ratings.count()
        
        try:
            get_all_ratings_avg = get_all_ratings_sum / get_all_ratings_cnt
            vendor_data = Vendor.objects.get(vendor_code = instance.vendor.vendor_code)
            vendor_data.quality_rating_avg = get_all_ratings_avg
            vendor_data.save()
        except ZeroDivisionError as e:
            return e.with_traceback()


@receiver(post_save, sender = Purchase_Order)
def avg_response_time(sender, instance, **kwargs):
    '''
    here, if in purchase_order model, status changed to completed and when vendor has acknowledged, 
    then we'll calculate average response time for those completed orders
    and store it in vendor model.
    '''
    if instance.status == 'Completed' and instance.acknowledgement_date is not None:
        # Calculate the difference between acknowledgement_date and issue_date in seconds
        date_diff_expression = ExpressionWrapper((F('acknowledgement_date') - F('issue_date')) / timedelta(seconds=1), output_field=fields.FloatField())
        
        # Filter purchase orders with non-null acknowledgement_date for the same vendor
        get_order_info = Purchase_Order.objects.filter(acknowledgement_date__isnull=False, vendor=instance.vendor)
        
        # Aggregate the average response time
        avg_response_time = get_order_info.aggregate(avg_response_time=Avg(date_diff_expression))['avg_response_time']
        
        # Update Vendor with the calculated average response time
        vendor_data = Vendor.objects.get(vendor_code = instance.vendor.vendor_code)
        vendor_data.average_response_time = avg_response_time
        vendor_data.save()
        

@receiver(post_save, sender = Purchase_Order)
def update_fulfillment_rate(sender, instance, **kwargs):
    '''
    here, if in purchase_order model, status changed to completed and when vendor has acknowledged, 
    then we'll calculate update fulfillment rate for those completed orders
    and store it in vendor model.
    '''
    if instance.status == 'Completed' and instance.acknowledgement_date is not None:
        # Count the number of successfully fulfilled purchased_orders (status 'Completed' without issues) for the given vendor
        fulfilled_order_count = Purchase_Order.objects.filter(
            vendor=instance.vendor,
            status='Completed',
            acknowledgement_date__isnull=False,
        ).count()

        # Count the total number of purchased_orders issued to the vendor
        total_order_count = Purchase_Order.objects.filter(vendor=instance.vendor).count()
        
        #calculate fulfillment rate
        try:
            fulfillment_rate = fulfilled_order_count / total_order_count 

            # Update Vendor with the calculated fulfillment time
            vendor_data = Vendor.objects.get(vendor_code = instance.vendor.vendor_code)
            vendor_data.average_response_time = fulfillment_rate
            vendor_data.save()

        except ZeroDivisionError as e:
            return e.with_traceback()
        
@receiver(post_save, sender = Vendor)
def update_historical_performance(sender, instance, **kwargs):
    '''
    here, we are making sure everytime, when all the given 4 fields 
    in vendor model are updated, we will update historical_performance model for the 
    given vendor
    '''

    if instance.on_time_delivery_rate is not None and instance.quality_rating_avg is not None and instance.avg_response_time is not None and instance.fulfillment_rate is not None:
        historical_performance_obj, _ = Historical_Performance.objects.get_or_create(vendor = instance)
        historical_performance_obj.on_time_delivery_rate = instance.on_time_delivery_rate
        historical_performance_obj.quality_rating_avg = instance.quality_rating_avg
        historical_performance_obj.avg