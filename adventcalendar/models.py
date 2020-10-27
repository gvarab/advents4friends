from django.db import models
from django.utils import timezone


class Calendar(models.Model):
    name = models.CharField(max_length=100)
    number_of_doors = models.IntegerField(default=24)

    def initialize_doors(self):
        for i in range(1, self.number_of_doors+1):
            Door.objects.create(number=i, content="", opening_date=timezone.now(), calendar=self)


class Door(models.Model):
    number = models.IntegerField()
    content = models.TextField(max_length=1000)
    opening_date = models.DateField(default=timezone.now)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, null=True)