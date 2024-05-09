from django.db import models
purchase_order_status = [("pending"), ("completed"), ("cancelled", "Cancelled")]

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField(max_length=500)
    address = models.TextField(max_length=10000)
    vendor_code = models.CharField(max_length=10,unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    avg_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

class Purchase_Order(models.Model):
    po_number = models.CharField(max_length=10, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=purchase_order_status, default="pending")
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgement_date = models.DateTimeField(null=True)

class Historical_Performance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()