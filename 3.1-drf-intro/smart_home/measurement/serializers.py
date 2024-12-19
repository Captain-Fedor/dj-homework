from rest_framework import serializers
from .models import Measurement, Sensor

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

class ListOfSensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']