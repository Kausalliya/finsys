# Generated by Django 4.1.7 on 2023-04-01 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0014_airportcode_stops_trip_rename_from_code_flight_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='no_of_stops',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='ticket_rate',
        ),
    ]
