from django.db import models
from django.utils import timezone


class Locations(models.Model):
    name = models.CharField(max_length=200)
    lat = models.FloatField()
    lon = models.FloatField()
    speed = models.FloatField()
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name


class SpeedLimits(models.Model):
    loc_id = models.ForeignKey(Locations, on_delete=models.CASCADE)
    limit = models.FloatField()


class EyeTracking(models.Model):
    loc_id = models.ForeignKey(Locations, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
