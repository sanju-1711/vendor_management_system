from django.urls import path
from . import views

urlpatterns = [
    path('', views.Ven.as_view()),
]