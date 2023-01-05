# Generated by Django 3.2.16 on 2023-01-04 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_table', '0011_alter_reservation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(choices=[(datetime.time(13, 0), '13:00'), (datetime.time(15, 0), '15:00'), (datetime.time(20, 0), '20:00'), (datetime.time(22, 0), '22:00')]),
        ),
    ]
