# analytics/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.db.models import Sum, Count
from trading.models import Order  # импортируем для примера торговой аналитики
from sales.models import SalesOrder  # импорт для аналитики продаж

class AnalyticsReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        # Пример: собираем аналитические данные для торговых ордеров и заказов
        trading_data = Order.objects.aggregate(
            total_orders=Count('id'),
            total_quantity=Sum('quantity'),
            total_value=Sum('price')
        )

        sales_data = SalesOrder.objects.aggregate(
            total_orders=Count('id'),
            total_amount=Sum('total_amount')
        )

        report = {
            'trading': trading_data,
            'sales': sales_data,
        }
        return Response(report)
