from django.urls import path
from src.presentation.rest_api.apps.authentication.views import RegisterAPIView

urlpatterns = [
    path("register/step/1/", RegisterAPIView.as_view({"post": "step1"})),
]
