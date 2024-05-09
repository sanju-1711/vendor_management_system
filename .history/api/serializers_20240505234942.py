from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.Serializer):
    class Meta:
        model = Vendor
        fields = ['name','']

    def create(self, validated_data):
        return Vendor.objects.create(**validated_data)