from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ExportCategoriesPDF(APIView):
    permission_classes = [AllowAny]  

    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="categories.pdf"'

        pdf = canvas.Canvas(response, pagesize=A4)
        pdf.drawString(100, 800, "Category Report")  
        pdf.drawString(100, 780, "----------------------------")

        y = 760  
        categories = Category.objects.all()

        for category in categories:
            pdf.drawString(100, y, f"ID: {category.id}, Name: {category.name}, Description: {category.description}")
            y -= 20  

        pdf.showPage()
        pdf.save()
        return response

class ExportProductsPDF(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="products.pdf"'

        pdf = canvas.Canvas(response, pagesize=A4)
        pdf.drawString(100, 800, "Product Report")  
        pdf.drawString(100, 780, "----------------------------")

        y = 760  
        products = Product.objects.all()

        for product in products:
            pdf.drawString(100, y, f"ID: {product.id}, Name: {product.name}, Price: ${product.price}, Category: {product.category}")
            y -= 20  

        pdf.showPage()
        pdf.save()
        return response

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
