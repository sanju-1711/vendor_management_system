from django.shortcuts import render
from django.http import response
from django.views import View
from .models import *
from .serializers import *

# Create your views here.
class VendorList(View):
    '''
    List all vendors or create a new vendor
    '''
    
    def get(self, request, format = None):
        Vendors = Vendor.objects.all()
        serializer = VendorSerializer(Ve, many = True)
        return response(serializer.data)