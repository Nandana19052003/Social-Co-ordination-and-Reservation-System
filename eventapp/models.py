from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    img=models.ImageField(upload_to="pic")
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Booking(models.Model):
    VENUE_CHOICES = [
        ("Orchid Ballroom", "The Orchid Ballroom"),
        ("Grand Oak", "Grand Oak Banquet"),
        ("Lotus Hall", "Lotus Event Hall"),
        ("Royal Crown", "The Royal Crown"),
        ("Blue Pearl", "Blue Pearl Pavilion"),
    ]

    cus_name = models.CharField(max_length=100)
    cus_ph = models.CharField(max_length=15)
    name = models.CharField(max_length=100)  # Event name
    booking_date = models.DateField()
    venue = models.CharField(max_length=100, choices=VENUE_CHOICES)

    def __str__(self):
        return self.cus_name


