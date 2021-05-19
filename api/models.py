from django.db import models

class Task(models.Model):
    username = models.CharField(max_length=100, unique=False)
    task_name = models.CharField(max_length=100, unique=True)
    task_tel = models.CharField(max_length=100)
    ice_type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    status  = models.BooleanField(null=False, default=False)
    time = models.TimeField(auto_now_add=True)

