from rest_framework import serializers
from . import models



class TemperatureSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'celsius', 'change', 'recorded_at',)
        model = models.Temperature
    
class HumiditySerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'rh', 'change', 'recorded_at')
        model = models.Humidity
        
class PressureSerializers(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'bp', 'change', 'recorded_at')
        model = models.Pressure 