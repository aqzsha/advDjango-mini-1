from django.contrib import admin
from .models import SalesOrder, SalesOrderItem, Invoice

admin.site.register(SalesOrder)
admin.site.register(SalesOrderItem)
admin.site.register(Invoice)
