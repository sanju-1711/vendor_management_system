from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View, API

# Create your views here.
class NewView(View):
    def get(self, request):
        return HttpResponse('Response')