# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Pareja(models.Model):
	pass

class Ceremonia(models.Model):
	pass

class Fiesta(models.Model):
	pass

class Luna_Miel(models.Model):
	pass

class Invitado(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)

	def __str__(self):
		return str(self.id)

class Sala(models.Model):
	id = models.CharField(max_length=20, primary_key=True)
	capacidad = models.IntegerField()

	def __str__(self):
		return str(self.id)

class Regalo(models.Model):
	id = models.AutoField(primary_key=True)
	tipo = models.CharField(max_length=5)
	descripcion = models.CharField(max_length=100)
	titular = models.ManyToManyField("Invitado", related_name="user")

	def __str__(self):
		return str(self.id)

class Mesa(models.Model):
	id = models.AutoField(primary_key=True)
	capacidad = models.IntegerField()
	sala = models.ManyToManyField("Sala")

	def __str__(self):
		return str(self.id)

class Camarero(models.Model):
	DNI = models.CharField(max_length=50, primary_key=True)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	inicio = models.CharField(max_length=50)
	final = models.CharField(max_length=50)
	mesa = models.ManyToManyField("Mesa")

	def __str__(self):
		return str(self.DNI)
