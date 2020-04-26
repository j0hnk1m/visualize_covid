# Generated by Django 3.0.4 on 2020-04-26 01:59

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_auto_20200425_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinate',
            name='latitude',
            field=models.DecimalField(decimal_places=4, max_digits=6, unique=True, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)]),
        ),
        migrations.AlterField(
            model_name='coordinate',
            name='longitude',
            field=models.DecimalField(decimal_places=4, max_digits=7, unique=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)]),
        ),
        migrations.AlterField(
            model_name='province',
            name='datetime',
            field=models.TimeField(default=datetime.datetime(2020, 4, 25, 18, 59, 5, 757986), verbose_name='datetime'),
        ),
    ]
