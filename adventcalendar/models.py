from django.db import models
from django.utils import timezone
from datetime import date, timedelta


class Calendar(models.Model):
    name = models.CharField(max_length=100)
    number_of_doors = models.IntegerField(default=24)
    start_date = models.DateField(default=date(timezone.now().year, 12, 1))

    def initialize_doors(self):
        for i in range(0, self.number_of_doors):
            Door.objects.create(number=i+1, content="", opening_date=self.start_date + timedelta(days=i),
                                calendar=self)


class Door(models.Model):
    number = models.IntegerField()
    content = models.TextField(max_length=1000)
    opening_date = models.DateField(default=timezone.now)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, null=True)