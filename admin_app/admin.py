from django.contrib import admin
from .models import Admin

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('admin_id', 'a_fname', 'a_lname', 'a_email', 'a_phone_no', 'user')
    search_fields = ('user', 'a_email', 'a_fname', 'a_lname')
