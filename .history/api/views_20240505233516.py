from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View

# Create your views here.
class Vendor(View):
    def get(self, request):
        return HttpResponse('Response')