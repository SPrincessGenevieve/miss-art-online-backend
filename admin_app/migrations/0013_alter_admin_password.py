# Generated by Django 5.1.2 on 2024-10-11 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0012_alter_admin_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$870000$ZcgR3IIL3mH3uVrF8Yi7li$6TvYmp+1y+O0FP0oM9Jidk4w7x4DWAl15RkGQAriGzM=', max_length=50),
        ),
    ]
