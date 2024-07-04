from rest_framework import routers
from src.presentation.rest_api.apps.currency.views import CurrencyAPIView

router = routers.DefaultRouter()
router.register(r"currencies", CurrencyAPIView, basename="currency")

urlpatterns = router.urls
