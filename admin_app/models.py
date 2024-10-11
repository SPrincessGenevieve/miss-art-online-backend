from django.db import models
from django.contrib.auth.hashers import make_password

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    a_fname = models.CharField(max_length=50)
    a_mname = models.CharField(max_length=50, blank=True)
    a_lname = models.CharField(max_length=50)
    a_email = models.EmailField()
    a_phone_no = models.CharField(max_length=15)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50, default=make_password('defaultpassword'))  # Default password

    def __str__(self):
        return self.user
