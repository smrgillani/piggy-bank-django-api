from django.db import models
import datetime

class Transactions(models.Model):
    user_id = models.CharField(max_length=11)
    child_id = models.CharField(max_length=255)
    ts_title = models.CharField(max_length=255)
    ts_amount = models.CharField(max_length=255)
    ts_date = models.CharField(max_length=200, default=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))