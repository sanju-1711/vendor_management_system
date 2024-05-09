from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('name', 'contact_details', 'address', 'vendor_code')
        read_only_fields = ['id']

    def create(self, validated_data):
        obj = Vendor.objects.create(**validated_data)
        obj.save()
        return obj
    
class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase_Order
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        obj = Purchase_Order.objects.create(**validated_data)
        obj.save()
        return obj
    
class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('name', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg', 'avg_response_time', 'fulfillment_rate')
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        instance.on_time_delivery_rate = validated_data.get('on_time_delivery_rate', instance.on_time_delivery_rate)
        instance.quality_rating_avg = validated_data.get('quality_rating_avg', instance.quality_rating_avg)

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historical_Performance
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        obj = Historical_Performance.objects.create(**validated_data)
        obj.save()
        return obj