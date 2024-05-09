from django.urls import path
from . import views

urlpatterns = [
    path('', views.VendorList.as_view()),
]