from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", include("docs")),
    path("admin/", admin.site.urls),
    path("lms/", include("lms.urls", namespace="lms")),
    path("users/", include("users.urls", namespace="users")),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema-swagger-ui'), name='swagger-ui'),
    path('redoc-ui/', SpectacularRedocView.as_view(url_name='schema-redoc'), name='redoc-ui'),
]
