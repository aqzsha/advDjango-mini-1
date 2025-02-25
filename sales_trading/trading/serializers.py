from rest_framework import serializers
from .models import Order, Transaction
from products.models import Product  # Импортируем модель продукта
from products.serializers import ProductSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product',
        write_only=True
    )

    class Meta:
        model = Order
        fields = ['id', 'user', 'order_type', 'product', 'product_id', 'quantity', 'price', 'status', 'created_at', 'updated_at']
        read_only_fields = ['status', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)

class TransactionSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), source='order', write_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'order', 'order_id', 'executed_price', 'executed_quantity', 'executed_at']
        read_only_fields = ['executed_at']
from rest_framework import serializers
from .models import Order, Transaction
from products.models import Product  # Импортируем модель продукта
from products.serializers import ProductSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product',
        write_only=True
    )

    class Meta:
        model = Order
        fields = ['id', 'user', 'order_type', 'product', 'product_id', 'quantity', 'price', 'status', 'created_at', 'updated_at']
        read_only_fields = ['status', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)

class TransactionSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), source='order', write_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'order', 'order_id', 'executed_price', 'executed_quantity', 'executed_at']
        read_only_fields = ['executed_at']
