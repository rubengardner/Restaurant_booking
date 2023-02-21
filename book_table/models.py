from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Table(models.Model):
    number_of_seats = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f'Table {self.id}, seats: {self.number_of_seats}'


class Reservation(models.Model):
    time_services = [
        ("13:00", "13:00"),
        ("15:00", '15:00'),
        ("20:00", '20:00'),
        ("22:00", '22:00')]
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='restaurant_booking'
    )
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    time = models.CharField(null=True, blank=False, choices=time_services, max_length=25)

    class Meta:
        unique_together = ["table", "date", "time"]

    def __str__(self):
        return f'{self.date}'
