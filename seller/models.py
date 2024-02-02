from django.db import models
import datetime

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    quantity = models.IntegerField(blank=True)
    date = models.DateField()
    quality = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name