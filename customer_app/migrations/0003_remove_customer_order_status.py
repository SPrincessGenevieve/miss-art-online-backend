# Generated by Django 5.1.2 on 2024-10-11 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0002_rename_status_customer_order_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='order_status',
        ),
    ]
