from django.db import models

# Create your models here.


class Demomodel(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField()
