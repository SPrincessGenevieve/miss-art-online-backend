# order_app/admin.py
from django.contrib import admin
from .models import Order  # Import your Order model

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_no', 'order_date', 'due_date', 'category', 'price', 'status']  # Customize as needed

admin.site.register(Order, OrderAdmin)  # Register the Order model with the custom admin
