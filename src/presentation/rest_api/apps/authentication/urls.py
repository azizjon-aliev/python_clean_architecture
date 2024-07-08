from django.urls import path
from src.presentation.rest_api.apps.authentication.views import (
    AuthAPIView,
)

urlpatterns = [
    path("register/step/1/", AuthAPIView.as_view({"post": "step1"})),
    path("login/", AuthAPIView.as_view({"post": "login"})),
    path("refresh-token/", AuthAPIView.as_view({"post": "refresh_token"})),
]
