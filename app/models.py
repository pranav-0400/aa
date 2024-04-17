from django.db import models

# Create your models here.

class UserTask(models.Model):
    kia=models.CharField(max_length=100)
