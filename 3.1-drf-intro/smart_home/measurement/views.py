# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from rest_framework.response import Response

from .models import *
from .serializers import *


class SensorsAPIview(generics.ListCreateAPIView):     # GET/POST sensors
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorAPIview(generics.RetrieveUpdateAPIView):  # GET/POST sensor
    queryset = Sensor.objects.all()
    serializer_class = SensorTempSerializer

class MeasurementsAPIview(generics.CreateAPIView):    # POST measurement
    queryset = Measurement.objects.all()
    serializer_class = TemperatureSerializer
