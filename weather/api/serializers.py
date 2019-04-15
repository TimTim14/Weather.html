from rest_framework import serializers
from . import models



class TemperatureSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'celsius', 'change', 'recorded_at',)
        model = models.Temperature