from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ExportUsersPDF

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('export-pdf/', ExportUsersPDF.as_view(), name='export_users_pdf'),
]
