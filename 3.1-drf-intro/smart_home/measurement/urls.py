from django.urls import path
from .views import *


urlpatterns = [
    path('sensors/', SensorsAPIview.as_view(), name='sensors'),
    path('sensors/<int:pk>/', SensorAPIview.as_view(), name='sensor_pk'),
    path('measurements/', MeasurementsAPIview.as_view(), name='measurements'),
    ]
