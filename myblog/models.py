from django.db import models

# Create your models here.
class blogs_db(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.TextField(max_length=20)
    tags = models.CharField(max_length=25)

class accounts(models.Model):
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Email = models.EmailField()