# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cotizacion', views.cotizacion, name='cotizacion'),
    path('logistica', views.logistica, name='logistica'),
    path('ahorro', views.ahorro, name='ahorro'),
    path('logistica/crear_sala', views.crear_sala, name='crear_sala'),
    path('logistica/crear_invitado', views.crear_invitado, name='crear_invitado'),
    path('logistica/crear_mesa', views.crear_mesa, name='crear_mesa'),
    path('logistica/crear_camarero', views.crear_camarero, name='crear_camarero'),
    path('logistica/listar_mesas', views.listar_mesas, name='listar_mesas'),
    path('logistica/listar_salas', views.listar_salas, name='listar_salas'),
    path('logistica/listar_camareros', views.listar_camareros, name='listar_camareros'),
    path('logistica/listar_invitados', views.listar_invitados, name='listar_invitados'),
    path('logistica/listar_regalos/<int:id_user>', views.listar_regalos, name='listar_regalos'),
    path('logistica/crear_regalo/<int:id_user>', views.crear_regalo, name='crear_regalos'),
    path('logistica/listar_todos_regalos', views.listar_todos_regalos, name='listar_todos_regalos'),
    path('cotizacion/pareja', views.pareja, name='pareja'),
    path('cotizacion/ceremonia', views.ceremonia, name='ceremonia'),
    path('cotizacion/fiesta', views.fiesta, name='fiesta'),
    path('cotizacion/luna_miel', views.luna_miel, name='luna_miel'),
]
