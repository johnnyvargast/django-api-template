from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

# Project urls
api_urlpatterns = [
    path('api/', include([
        path('', include('apps.commons.rest_api.urls', namespace='commons')),
        path('', include('apps.users.rest_api.urls', namespace='users')),
    ])),
]

# Swagger settings - API Documentation
schema_view = get_schema_view(
    openapi.Info(
        title='Backend API',
        default_version='v1',
    ),
    permission_classes=(AllowAny,),  # to access the documentation
    patterns=api_urlpatterns,
    public=True  # show all endpoints
)

# General URLs
urlpatterns = api_urlpatterns + [
    path('admin/', admin.site.urls),
    url(
        r'^' + settings.DOCUMENTATION_PATH_NAME + '(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    url(
        r'^' + settings.DOCUMENTATION_PATH_NAME + '/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    url(
        r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]

if not settings.USE_AMAZON_S3:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
