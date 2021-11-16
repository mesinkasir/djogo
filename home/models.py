from django.db import models
# Create your models here.

class Home (models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    cover =  models.CharField(max_length=500)
    section1 = models.TextField()
    imgsection1 = models.CharField(max_length=500)
    section2 = models.TextField()
    imgsection2 = models.CharField(max_length=500)
    imgfooter = models.CharField(max_length=500)
    footer = models.TextField()
    