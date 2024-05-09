from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View

# Create your views here.
def overview(request):
    return JsonResponse("API Base point", safe=False)