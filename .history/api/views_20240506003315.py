from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
        print("Vendors: ", Vendors)
        serializer = VendorSerializer(Vendors, many = True)
        print("Vendor serializer: " )
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid()    :
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)