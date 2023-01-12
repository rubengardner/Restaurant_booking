# Generated by Django 3.2.16 on 2023-01-04 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_table', '0007_alter_reservation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='time',
            field=models.TimeField(default='20:00:00'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together={('table', 'date', 'time')},
        ),
    ]