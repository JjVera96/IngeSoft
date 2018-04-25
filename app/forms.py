# -*- coding: utf-8 -*-
from django import forms
from .models import Invitado, Sala, Regalo, Mesa, Camarero, Boda, Pareja

class Invitado_Form(forms.ModelForm):
	class Meta:
		model = Invitado
		fields = ["nombre", "apellido"]

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