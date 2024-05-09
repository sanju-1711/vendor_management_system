from django.urls import path
from . import views

urlpatterns = [
    # path('token/', views.GenerateToken.as_view()),
    path('vendors/', views.VendorList.as_view()),
    path('vendors/<int:pk>/', views.VendorDetails.as_view()),
]