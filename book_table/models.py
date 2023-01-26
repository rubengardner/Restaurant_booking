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
        (datetime.time(13, 0, 0), "13:00"),
        (datetime.time(15, 0, 0), '15:00'),
        (datetime.time(20, 0, 0), '20:00'),
        (datetime.time(22, 0, 0), '22:00')]
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='restaurant_booking'
    )
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False, choices=time_services)

    class Meta:
        unique_together = ["table", "date", "time"]

    def __str__(self):
        return f'{self.date}'
