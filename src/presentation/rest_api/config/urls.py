from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from src.presentation.rest_api.apps.authentication.urls import urlpatterns as authentication_urls
from src.presentation.rest_api.apps.currency.urls import urlpatterns as currency_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/docs/download/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/v1/authentication/", include(authentication_urls)),
    path("api/v1/currency/", include(currency_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
