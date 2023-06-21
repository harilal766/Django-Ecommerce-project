from django.db import models

# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    confirm = models.CharField(max_length=20)
