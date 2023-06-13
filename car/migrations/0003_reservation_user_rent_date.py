# Generated by Django 4.2.2 on 2023-06-13 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_rename_availabilty_car_availability'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='reservation',
            constraint=models.UniqueConstraint(fields=('user', 'start_date', 'end_date'), name='user_rent_date'),
        ),
    ]
