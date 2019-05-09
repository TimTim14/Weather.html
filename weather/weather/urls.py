
from django.contrib import admin
from django.urls import path, include


from main import views
urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('chart/temp', views.LineChartView.as_view(), name='temp_chart'),
]
