# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import Invitado, Sala, Regalo, Mesa, Camarero, Boda, Pareja, Ceremonia, Fiesta, Luna_Miel

admin.site.register(Invitado)
admin.site.register(Sala)
admin.site.register(Regalo)
admin.site.register(Mesa)
admin.site.register(Camarero)
admin.site.register(Boda)
admin.site.register(Pareja)
admin.site.register(Fiesta)
admin.site.register(Luna_Miel)
