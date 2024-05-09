from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        obj = Vendor.objects.create(**validated_data)
        obj.save()
        return obj
    
class PurchaseOrder(serializers.ModelSerializer):
    class Meta:
        model = Purchase_Order
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        obj = Purchase_Order.objects.create(**validated_data)
        obj.save()
        return obj