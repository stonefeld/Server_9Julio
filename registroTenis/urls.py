from django.urls import path
from . import views

urlpatterns = [
    path('', views.respuesta, name='tenis-respuesta')
]
