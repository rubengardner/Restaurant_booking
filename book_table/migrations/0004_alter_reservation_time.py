# Generated by Django 3.2.16 on 2023-01-04 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_table', '0003_auto_20230104_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(default='20:00:00'),
        ),
    ]
