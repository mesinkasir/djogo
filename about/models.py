from django.db import models
# Create your models here.

class About (models.Model):
    name = models.CharField(max_length=100)
    cover = models.TextField()
    body = models.TextField()
    