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
    
    max_celsius = models.Temperature.objects.filter(recorded_at__range=(sometime_ago, now)).aggregate(Max('celsius'))['celsius__max']
    tmax = c2f(max_celsius)
    
    min_celsius = models.Temperature.objects.filter(recorded_at__range=(sometime_ago, now)).aggregate(Min('celsius'))['celsius__min']
    tmin =  c2f(min_celsius)
   
    max_rh = models.Humidity.objects.filter(recorded_at__range=(sometime_ago, now)).aggregate(Max('rh'))['rh__max']
    rhmax = (max_rh)
    
    min_rh = models.Humidity.objects.filter(recorded_at__range=(sometime_ago, now)).aggregate(Min('rh'))['rh__min']
    rhmin =  (min_rh)
   
    max_bp = models.Pressure.objects.filter(recorded_at__range=(sometime_ago, now)).aggregate(Max('bp'))['bp__max']
    bpmax = (max_bp)
    
    min_bp = models.Pressure.objects.filter(recorded_at__range=(sometime_ago, now)).aggregate(Min('bp'))['bp__min']
    bpmin =  (min_bp)
    
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
        'Pressure': Pressure,
        "tmin": tmin,
        "tmax": tmax,
        "rhmax": rhmax,
        "rhmin": rhmin,
        "bpmax": bpmax,
        "bpmin": bpmin}
    )

