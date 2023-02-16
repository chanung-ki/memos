from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class OneMemo(models.Model):
    content = models.CharField(max_length=100)
    writer = models.CharField(max_length=50)
    update_Date = models.DateTimeField(auto_now=True)
    write_date = models.DateTimeField(auto_now_add=True)
    

class Users(AbstractUser):
    pass