from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.Serializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        obj = Vendor.objects.create(**validated_data)
        return Vendor.objects.create(**validated_data)