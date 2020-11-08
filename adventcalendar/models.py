from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from datetime import date, timedelta
import random


class Calendar(models.Model):
    name = models.CharField(max_length=100)
    number_of_doors = models.IntegerField(default=24)
    start_date = models.DateField(default=date(timezone.now().year, 12, 1))

    class Theme(models.TextChoices):
        PLAIN = 'PL', _('Plain')
        RED = 'RE', _('Red with snowflakes')
        CUPCAKE = 'CU', _('Cupcakes and candy')
        TREE = 'TR', _('Christmas trees')
        TWIGS = 'TW', _('Twigs')
        SNOWMEN = 'SN', _('Snowmen')

    theme = models.CharField(
        max_length=2,
        choices=Theme.choices,
        default=Theme.PLAIN,
    )

    def initialize_doors(self):
        random.seed()
        random_door_numbers = list(range(0, self.number_of_doors))
        random.shuffle(random_door_numbers)
        for i, door_number in enumerate(random_door_numbers):
            Door.objects.create(
                number=i + 1,
                content="",
                opening_date=self.start_date + timedelta(days=i),
                calendar=self,
                position=door_number,
            )


class Door(models.Model):
    number = models.IntegerField()
    content = models.TextField(max_length=1000)
    opening_date = models.DateField(default=timezone.now)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, null=True)
    open = models.BooleanField(default=False)
    position = models.IntegerField()

    def short_content(self):
        short_content = self.content
        if len(self.content) > 10:
            short_content = short_content[0:10] + '...'
        return short_content
