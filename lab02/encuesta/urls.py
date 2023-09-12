from django.urls import path
from . import views

app_name = 'encuesta'

urlpatterns = [
    # ex: /encuesta/
    path('', views.index, name='index'),
    path('enviar', views.enviar, name = 'enviar'),
    path('calcular/', views.calcular, name='calcular'),
    path('calcular_cilindro/', views.calcular_cilindro, name='calcular_cilindro'),
]