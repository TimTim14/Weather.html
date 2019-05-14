from django.shortcuts import render
from api import models

from datetime import datetime, timedelta
from django.db.models import Max, Min, F
from datetime import datetime, timedelta

from chartjs.views.lines import BaseLineChartView

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

class LineChartView(BaseLineChartView):
    labels = []
    max_list = []
    min_list = []
    
    def set_minmax(self, index, item):
        if item > self.max_list[index]:
            self.max_list[index] = item
            
        if item < self.min_list[index]:
            self.min_list[index] = item
        
        
        
    def last_seven_days(self):
        now = datetime.now()
        seven_days_ago = now - timedelta(days=7)
        
        datas = models.Temperature.objects.order_by('-recorded_at').filter(recorded_at__range=(seven_days_ago,now)).annotate(value=F('fahrenheit'))
        
        
        for data in datas:
            weekday = datetime.weekday(data.recorded_at)
            print(str(data.recorded_at) + '=' + str(weekday) + '' + days[weekday])
            if days[weekday] not in self.labels:
                self.labels.append(days[weekday])
        
        self.max_list = [-100 for i in range(len(self.labels))]
        self.min_list = [9999 for i in range(len(self.labels))]
        
        for data in datas:
            weekday = datetime.weekday(data.recorded_at)
            idx = self.labels.index(days[weekday])
            self.set_minmax(idx, data.value)
        
    def get_providers(self):
        """ Return the names for the datasets. """
        return ['Max', 'Min']
        
    def get_labels(self):
        """ Return labels for our days. """
        return self.labels
    def get_data(self):
        """ Return min/max datasets to draw. """
        
        self.last_seven_days()
        
        return [self.max_list, self.min_list]

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

