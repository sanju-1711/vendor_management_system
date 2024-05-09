from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewView,name= 'api-overview'),
]