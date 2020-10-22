# Generated by Django 2.2.16 on 2020-10-22 16:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('content', models.CharField(max_length=1000)),
                ('opening_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
