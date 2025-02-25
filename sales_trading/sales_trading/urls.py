from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger Schema
schema_view = get_schema_view(
    openapi.Info(
        title="Sales & Trading API",
        default_version='v1',
        description="Документация для API проекта Sales & Trading",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Представление для рендеринга HTML
def home(request):
    return render(request, 'base/base.html')

urlpatterns = [
    # Главная страница
    path('', home, name='home'),

    # Аутентификация
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Приложения
    path('api/', include('users.urls')),
    path('api/', include('products.urls')),
    path('api/', include('trading.urls')),
    path('api/sales/', include('sales.urls')),
    path('api/analytics/', include('analytics.urls')),

    # Документация Swagger и Redoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Подключение статики в режиме DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
