from django.db import models

# Create your models here.
class PlaceDetails(models.Model):
    area = models.CharField(max_length=200,null=False)
    zone = models.CharField(max_length=200,null=False)
    time = models.TimeField(auto_now_add=True)
    people_frequency = models.IntegerField(default=0)
    police_station = models.BooleanField(default=True)
    bar = models.BooleanField(default=False)
    issafe = models.BooleanField(default=True)

    

    


