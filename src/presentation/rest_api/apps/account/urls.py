from django.urls import path
from src.presentation.rest_api.apps.account.views import RegisterAPIView

urlpatterns = [
    path("register/step/1/", RegisterAPIView.as_view({"post": "step1"})),
    path("register/step/2/", RegisterAPIView.as_view({"post": "step2"})),
]
