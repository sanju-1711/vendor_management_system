from django.db import models
purchase_order_status = [("Pending", "Pending"), ("Completed", "Completed"), ("Cancelled", "Cancelled")]

# Create your models here.
class Vendor(models.Model):
    '''
    to store all the Vendor related details
    '''
    name = models.CharField(max_length=100)
    contact_details = models.TextField(max_length=500)
    address = models.TextField(max_length=10000)
    vendor_code = models.CharField(max_length=10,unique=True)
    on_time_delivery_rate = models.FloatField(null=True)
    quality_rating_avg = models.FloatField(null=True)
    avg_response_time = models.FloatField(null=True)
    fulfillment_rate = models.FloatField(null=True)

class Purchase_Order(models.Model):
    '''
    to store all the order related details
    '''
    po_number = models.CharField(max_length=10, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=purchase_order_status, default="pending")
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgement_date = models.DateTimeField(null=True)

class Historical_Performance(models.Model):
    '''
    to store all the perfomance history details for all vendors
    '''
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now= True)
    on_time_delivery_rate = models.FloatField(null=True)
    quality_rating_avg = models.FloatField(null=True)
    average_response_time = models.FloatField(null=True)
    fulfillment_rate = models.FloatField(null=True)