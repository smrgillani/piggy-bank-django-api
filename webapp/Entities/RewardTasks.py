from django.db import models

class RewardTasks(models.Model):
    child_id = models.CharField(max_length=11)
    reward_task_title = models.CharField(max_length=255)
    reward_task_amount = models.CharField(max_length=255)