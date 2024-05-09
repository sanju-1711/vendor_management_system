from django.db.models.signals import pre_save, post_save
from django.db.models import F
from django.dispatch import receiver
from .models import *

'''
    Here django signals will be used to calculate real-time when PO related data is modified
'''

@receiver(post_save, sender = Purchase_Order)
def on_time_delivery_rate(sender, instance, **kwargs):
    '''
    here, when in purchase_order model, status changed to completed, 
    then we'll calculate on time delivery rate for those completed orders
    and store it in historical_performance model if no such row, 
    or update it
    '''
    if(instance.status == 'Completed'):
        total_completed_POs = Purchase_Order.objects.filter(status = 'Completed').count()
        completed_POs_before_delivery = Purchase_Order.objects.filter(
            status = 'Completed',
            delivery_date__lte = F('acknowledgement_date')
        ).count()

        try:
            delivery_rate_on_time = completed_POs_before_delivery / total_completed_POs
            obj = Historical_Performance.objects.get_or_create(vendor = instance.vendor)
            obj.on_time_delivery_rate = delivery_rate_on_time
            obj.save()
            print("on-time delivery rate is calculated successfully, here's its value: ", delivery_rate_on_time)
        except ZeroDivisionError as e:
            return e.with_traceback()
        
@receiver(post_save, sender = 'Purchase_Order')
def quality_rating_avg(sender, instance, **kwargs):
    if instance.quality_rating != None:
        get_all_ratings = Purchase_Order.objects.filter(quality_rating__isnull = False, vendor = instance.vendor)
        get_all_ratings_sum = get_all_ratings.aggregate(get_all_ratings_sum = sum('quality_rating'))['get_all_ratings_sum']
        get_all_ratings_cnt = get_all_ratings.count()
        
        try:
            get_all_ratings_avg = get_all_ratings_sum / get_all_ratings_cnt
            historical_data = Historical_Performance.objects.get_or_create(vendor = instance.vendor)
            historical_data.quality_rating_avg 