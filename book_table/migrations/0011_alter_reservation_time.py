# Generated by Django 3.2.16 on 2023-01-04 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_table', '0010_alter_reservation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(choices=[('13:00', '13:00'), ('15:00:00', '15:00'), ('20:00:00', '20:00'), ('22:00:00', '22:00')]),
        ),
    ]
