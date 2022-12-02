from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Table(models.Model):
    number_of_seats = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f'Table nº{self.id}'


class Reservation(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurant_booking')
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return f'Reservation: Customer {self.client}'
