from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path, include, re_path, reverse_lazy
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest.views import CustomAuthToken


openapi_info = openapi.Info(
  title="API rest example",
  default_version='v1',
  description="Test description",
  terms_of_service="https://www.google.com/policies/terms/",
  contact=openapi.Contact(email="cicerocasj@gmail.com"),
  license=openapi.License(name="BSD License"),
)
schema_view = get_schema_view(
   openapi_info,
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('schema-swagger-ui'))),
    path('admin/', admin.site.urls),
    path('v1/', include('rest.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', CustomAuthToken.as_view()),
    re_path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
