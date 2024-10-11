# customer_app/models.py
from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    c_fname = models.CharField(max_length=50)
    c_mname = models.CharField(max_length=50, blank=True)
    c_lname = models.CharField(max_length=50)
    c_phone_no = models.CharField(max_length=15)
    c_email = models.EmailField()

    def __str__(self):
        return f"{self.c_fname} {self.c_lname}"
