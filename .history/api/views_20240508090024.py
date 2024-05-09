from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.views import View
from .models import *
from .serializers import *
from django.db.models.signals import pre_save, post_save
from django.db.models import F
from django.dispatch import receiver

# Create your views here.

class VendorList(APIView):
    '''
    List all vendors or create a new vendor
    ''' 

    # permission_classes = [IsAuthenticated]
    
    def get(self, request, format = None):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many = True)
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
    List all orders or create a new order
    ''' 

    # permission_classes = [IsAuthenticated]
    
    def get(self, request, format = None):
        orders = Purchase_Order.objects.all()
        serializer = PurchaseOrderSerializer(orders, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
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
        #Returns an object instance
        try:
            return Purchase_Order.objects.get(pk = pk)
        except:
            raise Http404
        
    def get(self, request, pk, format=None):
        vendor = self.get_object(pk)
        serializer = PurchaseOrderSerializer(vendor)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        vendor = self.get_object(pk)
        serializer = PurchaseOrderSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
  
    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PerformanceEvaluation(APIView):
    '''
    to calculate following things for any given vendor on any value update: 
        - On-Time delivery rate
        - Quality Rating
        - Response Time
        - Fulfillment Rate
    '''

    def get_object(self, pk):
        #Returns an object instance
        try:
            return Historical_Performance.objects.get(pk = pk)
        except:
            raise Http404
    
    def get(self, request, pk, format=None):
        performance = self.get_object(pk)
        serializer = HistoricalPerformanceSerializer(performance)
        return Response(serializer.data)
    
    '''
    Here django signals will be used to calculate real-time when PO related data is modified
    '''

    @receiver(post_save, sender = Purchase_Order)
    def on_time_delivery_rate(self, sender, instance, **kwargs):
        if(instance.status == 'Completed'):
            total_completed_POs = Purchase_Order.objects.filter(status = 'Completed').count()
            completed_POs_before_delivery = Purchase_Order.objects.filter(
                status = 'Completed',
                delivery_date__lte = F('acknowledgement_date')
            ).count()

            try:
                delivery_rate_on_time = completed_POs_before_delivery / total_completed_POs
                obj = Historical_Performance.objects.get(vendor = instance.vendor)
                obj.on_time_delivery_rate = delivery_rate_on_time
                obj.save()
                print("Delivery_rate_on_time calculated successfully, here's its value: ", delivery_rate_on_time)
            except ZeroDivisionError as e:
                return e.with_traceback()
            
    # @receiver(post_save, sender = Purchase_Order)
    # def avg_quality_rading(self, sender, instance, **kwargs):
        
