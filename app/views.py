# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Invitado, Sala, Regalo, Mesa, Camarero
from .forms import Invitado_Form, Sala_Form, Regalo_Form, Mesa_Form, Camarero_Form


# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def cotizacion(request):
	context = {}
	return render(request, 'cotizacion.html', context)

def logistica(request):
	context = {}
	return render(request, 'logistica.html', context)

def ahorro(request):
	context = {}
	return render(request, 'ahorro.html', context)

def crear_sala(request):
	sala_form = Sala_Form(request.POST or None)
	context = {
		'sala_form' : sala_form
	}
	if sala_form.is_valid():
		form_data = sala_form.cleaned_data
		id = form_data.get("id")
		capacidad = form_data.get("capacidad")
		sala = Sala.objects.create(id=id, capacidad=capacidad)
		context = {
			'info' : 'Sala creada'
		}

	return render(request, 'crear_sala.html', context)

def crear_mesa(request):
	mesa_form = Mesa_Form(request.POST or None)
	salas = Sala.objects.all()
	context = {
		'mesa_form' : mesa_form,
		'salas' : salas
	}

	if mesa_form.is_valid():
		form_data = mesa_form.cleaned_data
		capacidad = form_data.get("capacidad")
		id_sala = form_data.get("sala")
		mesa = Mesa.objects.create(capacidad=capacidad)
		msala = Sala.objects.get(id=id_sala)
		mesa.sala.add(msala)
		context = {
			'info' : 'Mesa Creada'
		}

	return render(request, 'crear_mesa.html', context)

def crear_invitado(request):
	invitado_form = Invitado_Form(request.POST or None)
	context = {
		'invitado_form' : invitado_form
	}

	if invitado_form.is_valid():
		form_data = invitado_form.cleaned_data
		nombre = form_data.get("nombre")
		apellido = form_data.get("apellido")
		invitado = Invitado.objects.create(nombre=nombre, apellido=apellido)
		context = {
			'info' : 'Invitado Registrado'
		}

	return render(request, 'crear_invitado.html', context)

def crear_regalo(request, id_user):
	regalo_form = Regalo_Form(request.POST or None)
	titular = Invitado.objects.get(id=id_user)
	context = {
		'regalo_form' : regalo_form,
		'id_user' : id_user,
		'titular' : titular
	}

	if regalo_form.is_valid():
		form_data = regalo_form.cleaned_data
		tipo = form_data.get("tipo")
		descripcion = form_data.get("descripcion")
		regalo = Regalo.objects.create(tipo=tipo, descripcion=descripcion)
		regalo.titular.add(id_user)
		url = "/app/listar_regalos/{}".format(id_user)
		return HttpResponseRedirect(url)

	return render(request, 'crear_regalo.html', context)

def crear_camarero(request):
	camarero_form = Camarero_Form(request.POST or None)
	mesas = Mesa.objects.all()
	context = {
		'camarero_form' : camarero_form,
		'mesas' : mesas
	}

	if camarero_form.is_valid():

		form_data = camarero_form.cleaned_data
		dni = form_data.get("dni")
		nombre = form_data.get("nombre")
		apellido = form_data.get("apellido")
		inicio = form_data.get("inicio")
		final = form_data.get("final")
		idmesa = form_data.get("mesa")
		camarero = Camarero.objects.create(DNI=dni, nombre=nombre, apellido=apellido, inicio=inicio, final=final)
		amesa = Mesa.objects.get(id=idmesa)
		camarero.mesa.add(amesa)
		context = {
			'info' : 'Camarero Registrado'
		}

	return render(request, 'crear_camarero.html', context)

def listar_mesas(request):
	mesas = Mesa.objects.all()
	mode = True
	if not len(mesas):
		msg = "No hay Mesas para listar"
		mode = False
	else:
		msg = ""

	context = {
		'mesas' : mesas,
		'mode' : mode,
		'msg' : msg
	}

	return render(request, 'listar_mesas.html', context)

def listar_salas(request):
	salas = Sala.objects.all()
	mode = True
	if not len(salas):
		msg = "No hay Salas para listar"
		mode = False
	else:
		msg = ""

	context = {
		'salas' : salas,
		'mode' : mode,
		'msg' : msg
	}

	return render(request, 'listar_salas.html', context)

def listar_camareros(request):
	camareros = Camarero.objects.all()
	mode = True
	if not len(camareros):
		msg = "No hay Camareros para listar"
		mode = False
	else:
		msg = ""

	context = {
		'camareros' : camareros,
		'mode' : mode,
		'msg' : msg
	}

	return render(request, 'listar_camareros.html', context)

def listar_invitados(request):
	invitados = Invitado.objects.all()
	mode = True
	if not len(invitados):
		msg = "No hay Invitados para listar"
		mode = False
	else:
		msg = ""

	context = {
		'invitados' : invitados,
		'mode' : mode,
		'msg' : msg
	}

	return render(request, 'listar_invitados.html', context)

def listar_regalos(request, id_user):
	regalos = Regalo.objects.all().filter(titular=id_user)
	titular = Invitado.objects.get(id=id_user)
	mode = True
	if not len(regalos):
		msg = "No hay Regalos para listar"
		mode = False
	else:
		msg = ""

	context = {
		'regalos' : regalos,
		'mode' : mode,
		'msg' : msg,
		'titular' : titular
	}

	return render(request, 'listar_regalos.html', context)

def listar_todos_regalos(request):
	invitados = Invitado.objects.all()
	lista = []
	regalos = []
	for invitado in invitados:
		lista = list(Regalo.objects.all().filter(titular=invitado))
		for l in lista:
			regalo = {}
			regalo["tipo"] = l.tipo
			regalo["descripcion"] = l.descripcion
			regalo["titular"] = "{} {}".format(invitado.nombre, invitado.apellido)
			regalos.append(regalo)
	mode = True
	if not len(regalos):
		msg = "No hay Regalos para listar"
		mode = False
	else:
		msg = ""

	context = {
		'regalos' : regalos,
		'mode' : mode,
		'msg' : msg,
	}

	return render(request, 'listar_todos_regalos.html', context)