from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def overview(request):
    return JsonResponse("API Base point", safe=False)