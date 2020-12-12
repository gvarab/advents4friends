# Generated by Django 3.1.4 on 2020-12-12 14:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventcalendar', '0005_auto_20201129_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='number_of_doors',
            field=models.IntegerField(default=24, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(365)]),
        ),
    ]