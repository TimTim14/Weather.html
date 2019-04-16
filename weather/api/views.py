from rest_framework import generics

from . import models, serializers
# . import serializers TemperatureSerializer

class TemperatureList(generics.ListCreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    
class TemperatureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Temperature.objects.all()
    serializer_class = serializers.TemperatureSerializer
