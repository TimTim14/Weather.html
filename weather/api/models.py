from django.db import models

class Temperature(models.Model):
    celsius = models.FloatField(default=0.0)
    change = models.FloatField(default=0.0)
    recorded_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return str(self.celsius)
        
    
    
            
    @property
    def fahrenheit(self):
        "Returns the temperature in fahrenheit"
        return '%f' % ((self.celsius * 9/5) +32)
            
class Humidity(models.Model):
    rh = models.FloatField(default=0.0)
    change = models.FloatField(default=0.0)
    recorded_at = models.DateTimeField(auto_now=True)



class Pressure(models.Model):
    bp = models.FloatField(default=0.0)
    change = models.FloatField(default=0.0)
    recorded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.bp)


    

