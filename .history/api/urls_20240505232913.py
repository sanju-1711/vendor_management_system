from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewView.as_view(),name= 'api-overview'),
]