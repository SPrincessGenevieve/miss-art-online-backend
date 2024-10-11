# customer_app/admin.py
from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'c_fname', 'c_mname', 'c_lname', 'c_phone_no', 'c_email')

admin.site.register(Customer, CustomerAdmin)
