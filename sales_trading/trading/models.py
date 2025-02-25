from django.db import models
from django.conf import settings

class Order(models.Model):
    ORDER_TYPE_CHOICES = (
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    )

    STATUS_CHOICES = (
        ('open', 'Open'),
        ('executed', 'Executed'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    order_type = models.CharField(max_length=4, choices=ORDER_TYPE_CHOICES)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order_type.capitalize()} order by {self.user.username} for {self.product.name}"

class Transaction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='transactions')
    executed_price = models.DecimalField(max_digits=10, decimal_places=2)
    executed_quantity = models.PositiveIntegerField()
    executed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction for Order #{self.order.id} at {self.executed_price}"
