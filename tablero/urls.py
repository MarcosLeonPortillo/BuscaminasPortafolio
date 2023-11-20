from django.urls import path
from . import views #Importamos views para pasar las vistas

urlpatterns = [
    path('', views.index, name='index'), #en la pagina principal pasamos la vista index
    path('crea_tablero/', views.tablero, name='crea_tablero'), #pasamos la vista para crear el tablero
]