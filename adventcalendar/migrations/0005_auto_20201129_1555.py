# Generated by Django 3.1.3 on 2020-11-29 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventcalendar', '0004_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='content',
            field=models.TextField(max_length=10000),
        ),
    ]
