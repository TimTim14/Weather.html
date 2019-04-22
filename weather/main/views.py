from django.shortcuts import render
from api import models


def home(request):
    # Find the newest single temperature
    temp =   models.Temperature.objects.order_by('-recorded_at').first()
    # Gather the total number of temperature readings gathered.
    tcount = models.Temperature.objects.count()
    # Find the first temperature entry recorded
    tfirst = models.Temperature.objects.order_by('recorded_at').first()
    
    Humidity = models.Humidity.objects.order_by('recorded_at').first()
    Pressure = models.Pressure.objects.order_by('recorded_at').first()
    return render(request, 'home.html', {
        'temp': temp,
         'tcount': tcount, 
         'tfirst': tfirst.recorded_at,
        'Humidity': Humidity,
        'Pressure': Pressure}
    )

