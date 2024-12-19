from django.db import models


class Sensor(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, null=True, related_name='measurements')
    temperature = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)