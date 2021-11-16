from django.db import models
# Create your models here.

class Contact (models.Model):
    name = models.CharField(max_length=255)
    cover =  models.CharField(max_length=500)
    phone = models.CharField(max_length=60)
    whatsapp = models.CharField(max_length=60)
    email = models.CharField(max_length=255)
    address = models.TextField()
    