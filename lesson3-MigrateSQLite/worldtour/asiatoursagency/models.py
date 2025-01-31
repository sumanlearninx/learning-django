from django.db import models

# Create your models here.

class Tour(models.Model):
    origin_country = models.CharField(max_length=70)
    destination_country = models.CharField(max_length=70)
    number_of_nights = models.IntegerField()
    price = models.FloatField()
