from rest_framework import serializers
from .models import SalesOrder, SalesOrderItem, Invoice
from products.serializers import ProductSerializer
from products.models import Product

class SalesOrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product',
        write_only=True
    )

    class Meta:
        model = SalesOrderItem
        fields = ['id', 'product', 'product_id', 'quantity', 'price']

class SalesOrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(read_only=True)
    items = SalesOrderItemSerializer(many=True)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = SalesOrder
        fields = ['id', 'customer', 'created_at', 'status', 'total_amount', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        request = self.context.get('request')
        validated_data['customer'] = request.user
        order = SalesOrder.objects.create(**validated_data)
        total = 0
        for item_data in items_data:
            # Здесь можно рассчитать стоимость продукта, взять price из продукта или из запроса
            product = item_data['product']
            quantity = item_data['quantity']
            price = item_data.get('price') or product.price
            SalesOrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)
            total += price * quantity
        order.total_amount = total
        order.save()
        return order

class InvoiceSerializer(serializers.ModelSerializer):
    order = SalesOrderSerializer(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(queryset=SalesOrder.objects.all(), source='order', write_only=True)

    class Meta:
        model = Invoice
        fields = ['id', 'order', 'order_id', 'invoice_pdf', 'generated_at']
        read_only_fields = ['generated_at']
