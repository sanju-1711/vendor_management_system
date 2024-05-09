from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=100, null=False)
    contact_details = models.TextField(max_length=500, null=False)
    address = models.TextField(max_length=10000, null=False)
    vendor_code = models.CharField(max_length=10,unique=True, null=False)
    on_time_delivery_rate = models.FloatField(null=False)
    quality_rating_avg = models.FloatField(null=False)
    avg_response_time = models.FloatField(null=False)
    fulfillment_rate = models.FloatField(null=False)

class Purchase_Order(models.Model):
    po_number = models.CharField(max_length=10, unique=True, null=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=False)
    order_date = models.DateTimeField(null=False)
    delivery_date = models.DateTimeField(null=False)
    items = models.JSONField(null=False)
    quantity = models.IntegerField(null=False)
    status = models.CharField(max_length=20, null=False)
         = models.FloatField(null=False)
    issue_date = models.DateTimeField(null=False)
    acknowledgement_date = models.DateTimeField()

class Historical_Performance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()