# Generated by Django 4.1.7 on 2023-04-01 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0011_alter_testimonial_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
