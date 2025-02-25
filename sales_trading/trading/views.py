from rest_framework import viewsets, permissions
from .models import Order, Transaction
from .serializers import OrderSerializer, TransactionSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # можно настроить права доступа по необходимости

    def get_queryset(self):
        # Пример: возвращать только ордера текущего пользователя или все, если пользователь - админ
        user = self.request.user
        if user.is_staff:
            return Order.objects.all().order_by('-created_at')
        return Order.objects.filter(user=user).order_by('-created_at')

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('-executed_at')
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
