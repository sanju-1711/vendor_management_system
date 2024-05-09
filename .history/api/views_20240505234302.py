from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import View
from .models import *
from .serializers import *

# Create your views here.
class VendorList(APIView):
    '''
    List all vendors or create a new vendor
    '''
    
    def get(self, request, format = None):
        Vendors = Vendor.objects.all()
        serializer = VendorSerializer(Vendors, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=st)