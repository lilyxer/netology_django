from django.contrib import admin
from .models import *

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']             # что видим в админке
    search_fields = ['name']                           # поиск по полям
    list_filter = ['name', 'description']              # фильтрация

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['temperature', 'created_at', 'sensor']
    search_fields = ['sensor']
    list_filter = ['created_at', 'sensor'] 