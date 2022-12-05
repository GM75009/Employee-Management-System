from django.db import models

# Create your models here.
from django.contrib.auth.models import User


#1
class EmployeeDetail(models.Model):
    name = models.CharField(max_length=50)
    empcode = models.CharField(max_length=50)
    empdept = models.CharField(max_length=50)
    designations = models.CharField(max_length=50)
#2
class Addall(models.Model):
    name = models.CharField(max_length=50)
    Time = models.TimeField(max_length=50)
    Place = models.CharField(max_length=50)