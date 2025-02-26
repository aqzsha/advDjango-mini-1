from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('trader', 'Trader'),
        ('sales_rep', 'Sales Representative'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

    def __str__(self):
        return f"{self.username} ({self.role})"

    def is_admin(self):
        return self.role == 'admin'
    
    def is_trader(self):
        return self.role == 'trader'
    
    def is_sales_rep(self):
        return self.role == 'sales_rep'
    
    def is_customer(self):
        return self.role == 'customer'