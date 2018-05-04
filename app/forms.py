# -*- coding: utf-8 -*-
from django import forms
from .models import Invitado, Sala, Regalo, Mesa, Camarero, Boda, Pareja, Ceremonia, Fiesta, Luna_Miel

class Invitado_Form(forms.ModelForm):
	class Meta:
		model = Invitado
		fields = ["nombre", "apellido", "direccion"]

class Sala_Form(forms.ModelForm):
	class Meta:
		model = Sala
		fields = ["id", "capacidad"]

class Regalo_Form(forms.ModelForm):
	class Meta:
		model = Regalo
		fields = ["tipo", "descripcion"]

class Mesa_Form(forms.Form):
	capacidad = forms.CharField(max_length=50)
	sala = forms.CharField(max_length=50)

class Camarero_Form(forms.Form):
	dni = forms.CharField(max_length=50)
	nombre = forms.CharField(max_length=50)
	apellido = forms.CharField(max_length=50)
	inicio = forms.CharField(max_length=50)
	final = forms.CharField(max_length=50)
	mesa = forms.CharField(max_length=50)

class Boda_Form(forms.ModelForm):
	class Meta:
		model = Boda
		fields = ["nombre_novia", "apellido_novia", "nombre_novio", "apellido_novio", "fecha_hora", "personas"]

class Pareja_Form(forms.ModelForm):
	class Meta:
		model = Pareja
		fields = ["curso_pre", "argollas", "confirmacion_novia", "docs_novia", "vestido_novia", "maquillaje_peinado",
		"vestido_novia", "estetica", "confirmacion_novio" , "docs_novio", "vestido_novio"]

class Ceremonia_Form(forms.ModelForm):
	class Meta:
		model = Ceremonia
		fields = ["tipo", "abogado", "flores", "iglesia_fuera", "ceremonia", "ramo", "pajecitos", "carro_antiguo", 
		"coros", "boutonnieres", "servicio_fotografia"]

class Fiesta_Form(forms.ModelForm):
	class Meta:
		model = Fiesta
		fields = ["recordatorios", "musica", "tarjetas", "licores", "fuera_ciudad", "flores", "organizadora"]

class Luna_Miel_Form(forms.ModelForm):
	class Meta:
		model = Luna_Miel
		fields = ["viaje_colombia"]