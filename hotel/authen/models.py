from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.models import BaseUserManager
# Create your models here.





class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)

class Jobs(models.Model):
    job_name = models.CharField(max_length=100)
    job_description = models.CharField(max_length=100)


class Employer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    hire_date  = models.DateField()
    hourly_wage = models.IntegerField()
