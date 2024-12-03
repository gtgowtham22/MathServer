from django.urls import path
from . import views

urlpatterns = [
    path('', views.lamp_power_calculator, name='lamp_power_calculator'),
    path('calculate/', views.calculate_power, name='calculate_power'),
]
