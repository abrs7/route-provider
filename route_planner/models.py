# fuel_api/models.py
from django.db import models

class TruckStop(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"
