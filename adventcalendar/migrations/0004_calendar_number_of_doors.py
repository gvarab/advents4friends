# Generated by Django 2.2.16 on 2020-10-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventcalendar', '0003_auto_20201023_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='number_of_doors',
            field=models.IntegerField(default=24),
        ),
    ]
