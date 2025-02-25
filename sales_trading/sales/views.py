from rest_framework import viewsets, permissions
from .models import SalesOrder, Invoice
from .serializers import SalesOrderSerializer, InvoiceSerializer

class SalesOrderViewSet(viewsets.ModelViewSet):
    serializer_class = SalesOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Обычный пользователь видит только свои заказы, админ — все
        if user.is_staff:
            return SalesOrder.objects.all().order_by('-created_at')
        return SalesOrder.objects.filter(customer=user).order_by('-created_at')

class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Invoice.objects.all().order_by('-generated_at')
        # Пользователь видит счета только для своих заказов
        return Invoice.objects.filter(order__customer=user).order_by('-generated_at')
