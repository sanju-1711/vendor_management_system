from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        return Vendor.objects.create(**validated_data)
        # obj.save()
        # return obj