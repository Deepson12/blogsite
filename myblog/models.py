from django.db import models

# Create your models here.
class User(models.Model):
    Username = models.CharField(max_length=20)
    Email = models.EmailField()
    Password = models.CharField(max_length=25)