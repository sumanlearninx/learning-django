from django.db import models
class Tour(models.Model):
    origin_country = models.CharField(max_length = 70)
    destination_country = models.CharField(max_length = 70)
    number_of_nights = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        tour_id = getattr(self, 'id', 'not saved')
        return f"ID: {tour_id} From {self.origin_country} To {self.destination_country}, No. of nights {self.number_of_nights} and price ${self.price}"
