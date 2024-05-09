from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.views import View
from .models import *
from .serializers import *

# Create your views here.


class VendorList(APIView):
    '''
    List all vendors or create a new vendor
    ''' 

    # permission_classes = [IsAuthenticated]
    
    def get(self, request, format = None):
        Vendors = Vendor.objects.all()
        serializer = VendorSerializer(Vendors, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VendorDetails(APIView):
    '''
    Retrieve, update or delete specific vendor detail
    '''

    def get_object(self, pk):
        #Returns an object instance
        try:
            return Vendor.objects.get(pk = pk)
        except:
            raise Http404
        
    def get(self, request, pk, format=None):
        vendor = self.get_object(pk)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        vendor = self.get_object(pk)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
  
    def delete(self, request, pk, format=None):
        vendor = self.get_object(pk)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class PurchaseOrderList(APIView):
    '''
    List all orders or create a new vendor
    ''' 

    # permission_classes = [IsAuthenticated]
    
    def get(self, request, format = None):
        Vendors = Vendor.objects.all()
        serializer = VendorSerializer(Vendors, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VendorDetails(APIView):
    '''
    Retrieve, update or delete specific vendor detail
    '''

    def get_object(self, pk):
        #Returns an object instance
        try:
            return Vendor.objects.get(pk = pk)
        except:
            raise Http404
        
    def get(self, request, pk, format=None):
        vendor = self.get_object(pk)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        vendor = self.get_object(pk)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
  
    def delete(self, request, pk, format=None):
        vendor = self.get_object(pk)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)