from django.urls import path, include
from rest_framework import routers
from src.application.views.currency import CurrencyAPIView

router = routers.DefaultRouter()
router.register(r'currencies', CurrencyAPIView, basename='currency')

urlpatterns = [
    path('', include(router.urls))
]
