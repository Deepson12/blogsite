from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class blogs_db(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.TextField(max_length=20)
    tags = models.CharField(max_length=25)


