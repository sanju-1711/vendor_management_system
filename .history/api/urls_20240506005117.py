from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', views.GenerateToken.as_view()),
    path('vendors/', views.VendorList.as_view()),
]