from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Датчик')
    description = models.CharField(max_length=100, verbose_name='Расположение', 
                                   null=True, default='Датчик без имени')
    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class Measurement(models.Model):
    temperature = models.FloatField(max_length=4, verbose_name='Температура')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Время измерения')
    image = models.ImageField(null=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, 
                               related_name='measurements', verbose_name='Датчик')

    class Meta:
        verbose_name = 'Температура'
        verbose_name_plural = 'Температуры'
        ordering = ['sensor', 'created_at']

    def __str__(self) -> str:
        return str(self.temperature)