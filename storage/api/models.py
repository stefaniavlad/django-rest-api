from django.db import models


# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.location_name


class Item(models.Model):
    name = models.CharField(max_length=30)
    date_added = models.DateField(auto_now_add=True)
    location_name = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
