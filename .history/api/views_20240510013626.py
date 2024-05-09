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
        # to get all the vendors
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        # to create any new vendor
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
        # Returns a vendor object instance
        try:
            return Vendor.objects.get(pk = pk)
        except:
            raise Http404
        
    def get(self, request, pk, format=None):
        # to get any specific vendor object
        vendor = self.get_object(pk)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        # to update any specific vendor object
        vendor = self.get_object(pk)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
  
    def delete(self, request, pk, format=None):
        # to delete any specific vendor object
        vendor = self.get_object(pk)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class PurchaseOrderList(APIView):
    '''
    List all orders or create a new order
    ''' 

    # permission_classes = [IsAuthenticated]
    
    def get(self, request, format = None):
        # to get all the order lists
        orders = Purchase_Order.objects.all()
        serializer = PurchaseOrderSerializer(orders, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        # to create any new order
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PurchaseOrderDetails(APIView):
    '''
    Retrieve, update or delete specific order detail
    '''

    def get_object(self, pk):
        #Returns an order object instance
        try:
            return Purchase_Order.objects.get(pk = pk)
        except:
            raise Http404
        
    def get(self, request, pk, format=None):
        # to get any specific order object
        vendor = self.get_object(pk)
        serializer = PurchaseOrderSerializer(vendor)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        # to update any specific order object
        vendor = self.get_object(pk)
        serializer = PurchaseOrderSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
  
    def delete(self, request, pk, format=None):
        # to delete any specific order object
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PerformanceEvaluation(APIView):
    '''
    to fetch following things for any given vendor on any value update: 
        - On-Time delivery rate
        - Quality Rating
        - Response Time
        - Fulfillment Rate
    '''

    def get_object(self, pk):
        #Returns a vendor object instance
        try:
            return Vendor.objects.get(pk = pk)
        except:
            raise Http404
    
    def get(self, request, pk, format=None):
        performance = self.get_object(pk)
        serializer = VendorPerformanceSerializer(performance)
        return Response(serializer.data)
        
class HistoricalPerformance(APIView):
    '''
    to fetch following things for any given vendor on any value update: 
        - On-Time delivery rate
        - Quality Rating
        - Response Time
        - Fulfillment Rate
    '''

    def get_object(self, pk):
        #Returns a vendor object instance
        try:
            return Vendor.objects.get(pk = pk)
        except:
            raise Http404
    
    def get(self, request, pk, format=None):
        performance = self.get_object(pk)
        serializer = VendorPerformanceSerializer(performance)
        return Response(serializer.data)
        
