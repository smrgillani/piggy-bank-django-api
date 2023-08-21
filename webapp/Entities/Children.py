from django.db import models

class Children(models.Model):
    user_id = models.CharField(max_length=11)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=80)
    profile_pic = models.TextField()