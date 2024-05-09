from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.Serializer):
    class Meta:
        model = Vendor
        fields = ['name','contact_details', 'address', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg']

    def create(self, validated_data):
        return Vendor.objects.create(**validated_data)