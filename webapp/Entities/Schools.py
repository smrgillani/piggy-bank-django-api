from django.db import models
import datetime

class Schools(models.Model):
    logo = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    number = models.CharField(max_length=150)
    location = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    number_of_students = models.CharField(max_length=50)
    rp_name = models.CharField(max_length=150)
    rp_signature = models.CharField(max_length=250)
    rp_signature_file = models.CharField(max_length=50)
    rp_signature_date = models.CharField(max_length=50)
    principal_name = models.CharField(max_length=150)
    principal_signature = models.CharField(max_length=50)
    principal_signature_file = models.CharField(max_length=50)
    principal_signature_date = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50 , default=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))