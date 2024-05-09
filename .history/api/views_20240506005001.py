from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views import View
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class GenerateToken(APIView):
    def get(self, request):
        #Generate token
        refresh = RefreshToken.for_user(None)
        token = {
            'refresh': str(refresh)
            
        }

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