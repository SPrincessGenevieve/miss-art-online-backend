# Generated by Django 5.1.2 on 2024-10-11 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0015_alter_admin_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$870000$aksgXOwGy65nkvz2DrtIus$lgmA7dejWjbdpNgi6DVWQI0dryoZXwBuSm6qyslOTtc=', max_length=50),
        ),
    ]
