# Generated by Django 3.2.16 on 2023-01-04 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_table', '0005_auto_20230104_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
