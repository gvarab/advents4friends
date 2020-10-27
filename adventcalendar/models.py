from django.db import models
from django.utils import timezone


class Calendar(models.Model):
    name = models.CharField(max_length=100)
    number_of_doors = models.IntegerField(default=24)


class Door(models.Model):
    number = models.IntegerField()
    content = models.TextField(max_length=1000)
    opening_date = models.DateField(default=timezone.now)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, null=True)