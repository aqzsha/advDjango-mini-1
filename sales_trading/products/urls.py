from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ExportCategoriesPDF, ExportProductsPDF

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('export/categories/pdf/', ExportCategoriesPDF.as_view(), name='export_categories_pdf'),
    path('export/products/pdf/', ExportProductsPDF.as_view(), name='export_products_pdf'),
]
