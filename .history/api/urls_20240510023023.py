from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('vendors/', views.VendorList.as_view()),
    path('vendors/<int:pk>/', views.VendorDetails.as_view()),
    path('purchase_orders/', views.PurchaseOrderList.as_view()),
    path('purchase_orders/<int:pk>/', views.PurchaseOrderDetails.as_view()),
    path('purchase_orders/<int:pk>/acknowledge', views.UpdatePurchaseAcknowledgement.as_view()),
    path('vendors/<int:pk>/performance', views.PerformanceEvaluation.as_view()),
    path('history/<int:pk>/performance', views.HistoricalPerformance.as_view()),
]