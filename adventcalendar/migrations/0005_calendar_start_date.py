# Generated by Django 2.2.16 on 2020-10-27 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventcalendar', '0004_calendar_number_of_doors'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='start_date',
            field=models.DateField(default=datetime.date(2020, 12, 1)),
        ),
    ]
