# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cotizacion', views.cotizacion, name='cotizacion'),
    path('logistica', views.logistica, name='logistica'),
    path('ahorro', views.ahorro, name='ahorro'),
    path('cotizacion/crear_sala', views.crear_sala, name='crear_sala'),
    path('cotizacion/crear_invitado', views.crear_invitado, name='crear_invitado'),
    path('cotizacion/crear_mesa', views.crear_mesa, name='crear_mesa'),
    path('cotizacion/crear_camarero', views.crear_camarero, name='crear_camarero'),
    path('listar_mesas', views.listar_mesas, name='listar_mesas'),
    path('listar_salas', views.listar_salas, name='listar_salas'),
    path('listar_camareros', views.listar_camareros, name='listar_camareros'),
    path('listar_invitados', views.listar_invitados, name='listar_invitados'),
    path('listar_regalos', views.listar_regalos, name='listar_regalos'),
    
]
