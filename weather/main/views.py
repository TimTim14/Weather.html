from django.shortcuts import render
from api import models

from datetime import datetime, timedelta
from django.db.models import Max, Min


def c2f(celsius):
    return ((celsius * 9/5) + 32)


def home(request):
    now = datetime.now()
    sometime_ago = now - timedelta(days=7)
    temp =   models.Temperature.objects.order_by('-recorded_at').first()
    
    max_celsius = models.Temperature.objects.filter(recorded_at__range=(sometime_ago, now)).aggregate(Min('celsius'))
    tmax = c2f(max_celsius)
        
    min_celsius = models.Temperature.objects.filter(recorded_at__range=(sometime_ago, now)).aggregate(Min('celsius'))
    tmin = c2f(min_celsius)
   
   
    tcount = models.Temperature.objects.count()
    # Find the first temperature entry recorded
    tfirst = models.Temperature.objects.order_by('recorded_at').first()
    
    Humidity = models.Humidity.objects.order_by('-recorded_at').first()
    Pressure = models.Pressure.objects.order_by('-recorded_at').first()
    return render(request, 'home.html', {
        'temp': temp,
         'tcount': tcount, 
         'tfirst': tfirst.recorded_at,
        'Humidity': Humidity,
        'Pressure': Pressure}
    )

