from django.db import models
import datetime

class Diary(models.Model):
    title = models.CharField(max_length=256)
    username=models.CharField(max_length=256)
    detail = models.TextField(default='')
    created = models.DateTimeField(default=datetime.datetime.now)
    username = models.CharField(max_length=256)
   
# Create your models here.
