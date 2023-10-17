from rest_framework import serializers
from .models import *


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor                          # берем поля класса которые будут доступны в основном классе
        fields = '__all__'                      # те поля что будем возвращать в json
    

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'
    

class SensorTempSerializer(serializers.ModelSerializer):
    measurements = TemperatureSerializer(many=True, read_only=True)
    class Meta:
        model = Sensor
        fields = '__all__'