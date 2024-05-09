from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True)
    contact_details = serializers.TextField(max_length=500, required)
    address = serializers.TextField(max_length=10000, null=False)
    vendor_code = serializers.CharField(max_length=10,unique=True, null=False)
    on_time_delivery_rate = serializers.FloatField(null=False)
    quality_rating_avg = serializers.FloatField(null=False)
    avg_response_time = serializers.FloatField(null=False)
    fulfillment_rate = serializers.FloatField(null=False)

    def create(self, validated_data):
        return Vendor.objects.create(**validated_data)