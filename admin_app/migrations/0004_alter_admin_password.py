# Generated by Django 5.1.2 on 2024-10-11 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_alter_admin_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$870000$LmlxXPjo7LygGbF3lCWjoR$N+eFPdfPvY8xp3s3zp+VAFIWcsRi3GJ+ZD03sd9/m1M=', max_length=50),
        ),
    ]
