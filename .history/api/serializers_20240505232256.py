from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, null=False)
    contact_details = models.TextField(max_length=500, null=False)
    address = models.TextField(max_length=10000, null=False)
    vendor_code = models.CharField(max_length=10,unique=True, null=False)
    on_time_delivery_rate = models.FloatField(null=False)
    quality_rating_avg = models.FloatField(null=False)
    avg_response_time = models.FloatField(null=False)
    fulfillment_rate = models.FloatField(null=False)