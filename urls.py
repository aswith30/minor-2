from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict, name='predict'),
    path('result/', views.result, name='result'),
    path('predict/bmi/', views.bmi_calculator, name='bmi_calculator'),
]
