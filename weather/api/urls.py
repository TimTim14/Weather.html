from django.urls import path

from . import views

urlpatterns = [
    path('', views.TemperatureList.as_view()),
    path('<int:pk>/', views.TemperatureDetail.as_view()),
    path('', views.HumidityList.as_view()),
    path('<int:pk>/', views.HumidityDetail.as_view()),
    path('', views.PressureList.as_view()),
    path('<int:pk>/', views.PressureDetail.as_view()),
    ]
    
