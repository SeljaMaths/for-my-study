from django.db import models

# Create your models here.


class employee_details(models.Model):
    Name = models.CharField(max_length=200)
    email = models.CharField(unique=True, max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
