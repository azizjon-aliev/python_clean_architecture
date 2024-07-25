from django.urls import path
from src.presentation.rest_api.apps.authentication.views import (
    AuthAPIView,
)

urlpatterns = [
    path("register/", AuthAPIView.as_view({"post": "register"})),
    path("login/", AuthAPIView.as_view({"post": "login"})),
    path("refresh-token/", AuthAPIView.as_view({"post": "refresh_token"})),
]
