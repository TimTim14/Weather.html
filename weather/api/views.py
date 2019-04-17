from rest_framework import generics

from . import models, serializers
# . import serializers TemperatureSerializer

class TemperatureList(generics.ListCreateAPIView):
    queryset = models.Temperature.objects.all()
    serializer_class = serializers.TemperatureSerializer
    
class TemperatureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Temperature.objects.all()
    serializer_class = serializers.TemperatureSerializer

class HumidityList(generics.ListCreateAPIView):
    queryset = models.Humidity.objects.all()
    serializers_class = serializers.HumiditySerializer
    
class HumidityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Humidity.objects.all()
    serializer_class = serializers.TemperatureSerializer
    
class PressureList(generics.ListCreateAPIView):
    queryset = models.Pressure.objects.all()
    serializers_class = serializers.HumiditySerializer
    
class PressureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Pressure.objects.all()
    serializer_class = serializers.TemperatureSerializer
