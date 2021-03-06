# -*- coding: utf-8 -*-
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from django.http import HttpResponseRedirect, HttpResponse
from .models import Invitado, Sala, Regalo, Mesa, Camarero, Pareja, Boda, Ceremonia, Fiesta, Luna_Miel
from .forms import Invitado_Form, Sala_Form, Regalo_Form, Mesa_Form, Camarero_Form, Boda_Form, Pareja_Form, Ceremonia_Form, Fiesta_Form, Luna_Miel_Form


# Create your views here.
def index(request):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	context = {
		'costos' : costos
	}

	return render(request, 'index.html', context)

def cotizacion(request):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	context = {
		'costos' : costos
	}

	return render(request, 'cotizacion.html', context)

def logistica(request):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	context = {
		'costos' : costos
	}

	return render(request, 'logistica.html', context)

def ahorro(request):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	context = {
		'costos' : costos
	}

	return render(request, 'ahorro.html', context)

def comida(request):
	bodas = Boda.objects.all()
	titulo = 'Comida'
	descripcion = 'Las estaciones de comida casuales no son solo divertidas, sino también una forma de ahorrar en comparación con una cena formal.'
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	context = {
		'costos' : costos,
		'titulo' : titulo,
		'descripcion' : descripcion
	}

	return render(request, 'ahorros.html', context)

def accesorios(request):
	bodas = Boda.objects.all()
	titulo = 'Accesorios'
	descripcion = 'Cómo dice la tradición, toda novia debe llevar algo prestado el día de su boda entonces, ¿qué tal si pides el velo prestado? ¿o los aretes? ¿el tocado para el peinado?'
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	context = {
		'costos' : costos,
		'titulo' : titulo,
		'descripcion' : descripcion
	}

	return render(request, 'ahorros.html', context)

def pastel(request):
	bodas = Boda.objects.all()
	titulo = 'Pastel'
	descripcion = 'No necesitas un pastel tamaño gigante para la boda, puedes disponer uno pequeño en forma de exhibición para las fotos y la decoración, y servir a tus invitados la opción de postre que ofrecen en el lugar del banquete.'
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	context = {
		'costos' : costos,
		'titulo' : titulo,
		'descripcion' : descripcion
	}

	return render(request, 'ahorros.html', context)

def recordatorios(request):
	bodas = Boda.objects.all()
	titulo = 'Recordatorios'
	descripcion = 'Son un detalle muy lindo y especial, pero cuando se trata de ahorrar, hay que pensar en todo y los recordatorios no son obligatorios.'
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	context = {
		'costos' : costos,
		'titulo' : titulo,
		'descripcion' : descripcion
	}

	return render(request, 'ahorros.html', context)

def en_casa(request):
	bodas = Boda.objects.all()
	titulo = 'En Casa'
	descripcion = 'Organizar el matrimonio en casa es una opción ideal para un matrimonio íntimo y de poco presupuesto.'
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	context = {
		'costos' : costos,
		'titulo' : titulo,
		'descripcion' : descripcion
	}

	return render(request, 'ahorros.html', context)

def crear_sala(request):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	sala_form = Sala_Form(request.POST or None)
	context = {
		'costos' : costos,
		'sala_form' : sala_form
	}
	if sala_form.is_valid():
		form_data = sala_form.cleaned_data
		id = form_data.get("id")
		capacidad = form_data.get("capacidad")
		sala = Sala.objects.create(id=id, capacidad=capacidad)
		context = {
			'costos' : costos,
			'info' : 'Sala creada'
		}

	return render(request, 'crear_sala.html', context)

def crear_mesa(request):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	mesa_form = Mesa_Form(request.POST or None)
	salas = Sala.objects.all()
	context = {
		'costos' : costos,
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
			'costos' : costos,
			'info' : 'Mesa Creada'
		}

	return render(request, 'crear_mesa.html', context)

def crear_invitado(request):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	invitado_form = Invitado_Form(request.POST or None)
	context = {
		'costos' : costos,
		'invitado_form' : invitado_form
	}

	if invitado_form.is_valid():
		form_data = invitado_form.cleaned_data
		nombre = form_data.get("nombre")
		apellido = form_data.get("apellido")
		direccion = form_data.get("direccion")
		invitado = Invitado.objects.create(nombre=nombre, apellido=apellido, direccion=direccion)
		context = {
			'costos' : costos,
			'info' : 'Invitado Registrado'
		}

	return render(request, 'crear_invitado.html', context)

def crear_regalo(request, id_user):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	regalo_form = Regalo_Form(request.POST or None)
	titular = Invitado.objects.get(id=id_user)
	context = {
		'costos' : costos,
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
		url = "/logistica/listar_regalos/{}".format(id_user)
		return HttpResponseRedirect(url)

	return render(request, 'crear_regalo.html', context)

def crear_camarero(request):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"
	
	camarero_form = Camarero_Form(request.POST or None)
	mesas = Mesa.objects.all()
	context = {
		'costos' : costos,
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
			'costos' : costos,
			'info' : 'Camarero Registrado'
		}

	return render(request, 'crear_camarero.html', context)

def listar_mesas(request):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"
	
	salas = Sala.objects.all()
	lista = []
	mesas = []
	for sala in salas:
		lista = list(Mesa.objects.all().filter(sala=sala))
		for l in lista:
			mesa = {}
			mesa["id"] = l.id
			mesa["capacidad"] = l.capacidad
			mesa["sala"] = sala
			mesas.append(mesa)
	mode = True
	if not len(mesas):
		msg = "No hay Mesas para listar"
		mode = False
	else:
		msg = ""

	context = {
		'costos' : costos,
		'mesas' : mesas,
		'mode' : mode,
		'msg' : msg
	}
	
	return render(request, 'listar_mesas.html', context)

def listar_salas(request):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	salas = Sala.objects.all()
	mode = True
	if not len(salas):
		msg = "No hay Salas para listar"
		mode = False
	else:
		msg = ""

	context = {
		'costos' : costos,
		'salas' : salas,
		'mode' : mode,
		'msg' : msg
	}

	return render(request, 'listar_salas.html', context)

def listar_camareros(request):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	lista = Camarero.objects.all()
	camareros = []	
	for l in lista:
		camarero = {}
		camarero["DNI"] = l.DNI
		camarero["nombre"] = l.nombre
		camarero["apellido"] = l.apellido
		camarero["inicio"] = l.inicio
		camarero["final"] = l.final
		ms = Camarero.objects.values("mesa").filter(DNI = l.DNI)
		mesas = []
		for m in ms:
			mesas.append(str(m["mesa"]))
		camarero["mesa"] = '-'.join(mesas)
		camareros.append(camarero)
	mode = True
	if not len(camareros):
		msg = "No hay Camareros para listar"
		mode = False
	else:
		msg = ""

	context = {
		'costos' : costos,
		'camareros' : camareros,
		'mode' : mode,
		'msg' : msg
	}

	return render(request, 'listar_camareros.html', context)

def listar_invitados(request):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	invitados = Invitado.objects.all()
	mode = True
	if not len(invitados):
		msg = "No hay Invitados para listar"
		mode = False
	else:
		msg = ""

	context = {
		'costos' : costos,
		'invitados' : invitados,
		'mode' : mode,
		'msg' : msg
	}

	return render(request, 'listar_invitados.html', context)

def listar_regalos(request, id_user):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	regalos = Regalo.objects.all().filter(titular=id_user)
	titular = Invitado.objects.get(id=id_user)
	mode = True
	if not len(regalos):
		msg = "No hay Regalos para listar"
		mode = False
	else:
		msg = ""

	context = {
		'costos' : costos,	
		'regalos' : regalos,
		'mode' : mode,
		'msg' : msg,
		'titular' : titular
	}

	return render(request, 'listar_regalos.html', context)

def listar_todos_regalos(request):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

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
		'costos' : costos,
		'regalos' : regalos,
		'mode' : mode,
		'msg' : msg,
	}

	return render(request, 'listar_todos_regalos.html', context)

def pareja(request):
	boda = Boda.objects.all()
	
	if not len(boda):
		boda_form = Boda_Form(request.POST or None)
		pareja_form = Pareja_Form(request.POST or None)
		context = {
			'costos' : '0$-0$',
			'boda_form' : boda_form,
			'pareja_form' : pareja_form
		}

		if boda_form.is_valid() and pareja_form.is_valid():
			form_data = boda_form.cleaned_data
			nombre_novia = form_data.get("nombre_novia")
			apellido_novia = form_data.get("apellido_novia")
			nombre_novio = form_data.get("nombre_novio")
			apellido_novio = form_data.get("apellido_novio")
			fecha_hora = form_data.get("fecha_hora")
			personas = form_data.get("personas")
			costo_bajo = 0
			costo_alto = 0
			form_data = pareja_form.cleaned_data
			curso_pre = form_data.get("curso_pre")
			argollas = form_data.get("argollas")
			confirmacion_novia = form_data.get("confirmacion_novia")
			docs_novia = form_data.get("docs_novia")
			vestido_novia = form_data.get("vestido_novia")
			maquillaje_peinado = form_data.get("maquillaje_peinado")
			estetica = form_data.get("estetica")
			confirmacion_novio = form_data.get("confirmacion_novio")
			docs_novio = form_data.get("docs_novio")
			vestido_novio = form_data.get("vestido_novio")

			new_boda = Boda.objects.create(nombre_novia=nombre_novia, apellido_novia=apellido_novia, nombre_novio=nombre_novio,
				apellido_novio=apellido_novio, fecha_hora=fecha_hora, personas=personas, costo_bajo=costo_bajo, 
				costo_alto=costo_alto)
			pareja = Pareja.objects.create(curso_pre=curso_pre, argollas=argollas, confirmacion_novia=confirmacion_novia,
				docs_novia=docs_novia, vestido_novia=vestido_novia, maquillaje_peinado=maquillaje_peinado,
				estetica=estetica, confirmacion_novio=confirmacion_novio, docs_novio=docs_novio, vestido_novio=vestido_novio)

			calcular_costos()
			return HttpResponseRedirect('pareja')

		return render(request, 'pareja.html', context)

	else:
		up_pareja = Pareja.objects.all()[0]
		up_boda = Boda.objects.all()[0]	
		costos = "{}$ - {}$".format(up_boda.costo_bajo, up_boda.costo_alto)
		boda_form = Boda_Form(request.POST or None, instance=up_boda)
		pareja_form = Pareja_Form(request.POST or None, instance=up_pareja)
		context = {
			'costos' : costos,
			'boda_form' : boda_form,
			'pareja_form' : pareja_form
		}

		if boda_form.is_valid() and pareja_form.is_valid():
			form_data = boda_form.cleaned_data
			up_boda.nombre_novia = form_data.get("nombre_novia")
			up_boda.apellido_novia = form_data.get("apellido_novia")
			up_boda.nombre_novio = form_data.get("nombre_novio")
			up_boda.apellido_novio = form_data.get("apellido_novio")
			up_boda.fecha_hora = form_data.get("fecha_hora")
			up_boda.personas = form_data.get("personas")
			form_data = pareja_form.cleaned_data
			up_pareja.curso_pre = form_data.get("curso_pre")
			up_pareja.argollas = form_data.get("argollas")
			up_pareja.confirmacion_novia = form_data.get("confirmacion_novia")
			up_pareja.docs_novia = form_data.get("docs_novia")
			up_pareja.vestido_novia = form_data.get("vestido_novia")
			up_pareja.maquillaje_peinado = form_data.get("maquillaje_peinado")
			up_pareja.estetica = form_data.get("estetica")
			up_pareja.confirmacion_novio = form_data.get("confirmacion_novio")
			up_pareja.docs_novio = form_data.get("docs_novio")
			up_pareja.vestido_novio = form_data.get("vestido_novio")
			up_boda.save()
			up_pareja.save()
			calcular_costos()
			return HttpResponseRedirect('pareja')

		context = {
			'costos' : costos,
			'identificacion' : up_boda,
			'boda_form' : boda_form,
			'pareja_form' : pareja_form,
			'nombre_novia' : up_boda.nombre_novia,
			'apellido_novia' : up_boda.apellido_novia,
			'nombre_novio' : up_boda.nombre_novio,
			'apellido_novio' : up_boda.apellido_novio,
			'fecha_hora' : up_boda.fecha_hora,
			'personas' : up_boda.personas,
			'curso_pre' : up_pareja.curso_pre,
			'argollas' : up_pareja.argollas,
			'confirmacion_novia' : up_pareja.confirmacion_novia,
			'docs_novia' : up_pareja.docs_novia,
			'vestido_novia' : up_pareja.vestido_novia,
			'maquillaje_peinado' : up_pareja.maquillaje_peinado,
			'vestido_novia' : up_pareja.vestido_novia,
			'estetica' : up_pareja.estetica,
			'confirmacion_novio' : up_pareja.confirmacion_novio,
			'docs_novio' : up_pareja.docs_novio,
			'vestido_novio' : up_pareja.vestido_novio
		}

	return render(request, 'pareja_edit.html', context)

def ceremonia(request):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	cere = Ceremonia.objects.all()
	
	if not len(cere):
		cere_form = Ceremonia_Form(request.POST or None)
		context = {
			'costos' : costos,
			'cere_form' : cere_form
		}

		if cere_form.is_valid():
			form_data = cere_form.cleaned_data
			tipo = form_data.get("tipo")
			abogado = form_data.get("abogado")
			flores = form_data.get("flores")
			iglesia_fuera = form_data.get("iglesia_fuera")
			ceremonia = form_data.get("ceremonia")
			ramo = form_data.get("ramo")
			pajecitos = form_data.get("pajecitos")
			carro_antiguo = form_data.get("carro_antiguo")
			coros = form_data.get("coros")
			boutonnieres = form_data.get("boutonnieres")
			servicio_fotografia = form_data.get("servicio_fotografia")

			new_cere = Ceremonia.objects.create(tipo=tipo, abogado=abogado, flores=flores, iglesia_fuera=iglesia_fuera, 
				ceremonia=ceremonia, ramo=ramo, pajecitos=pajecitos, carro_antiguo=carro_antiguo, coros=coros, 
				boutonnieres=boutonnieres, servicio_fotografia=servicio_fotografia)

			calcular_costos()
			return HttpResponseRedirect('ceremonia')

		return render(request, 'ceremonia.html', context)

	else:
		up_cere = Ceremonia.objects.all()[0]
		
		cere_form = Ceremonia_Form(request.POST or None, instance=up_cere)
		context = {
			'cere_form' : cere_form
		}

		if cere_form.is_valid():
			form_data = cere_form.cleaned_data
			up_cere.tipo = form_data.get("tipo")
			up_cere.abogado = form_data.get("abogado")
			up_cere.flores = form_data.get("flores")
			up_cere.iglesia_fuera = form_data.get("iglesia_fuera")
			up_cere.ceremonia = form_data.get("ceremonia")
			up_cere.ramo = form_data.get("ramo")
			up_cere.pajecitos = form_data.get("pajecitos")
			up_cere.carro_antiguo = form_data.get("carro_antiguo")
			up_cere.coros = form_data.get("coros")
			up_cere.boutonnieres = form_data.get("boutonnieres")
			up_cere.servicio_fotografia = form_data.get("servicio_fotografia")
			up_cere.save()
			calcular_costos()
			return HttpResponseRedirect('ceremonia')

		context = {
			'costos' : costos,
			'cere_form' : cere_form,
			'tipo' : up_cere.tipo,
			'abogado' : up_cere.abogado,
			'flores' : up_cere.flores,
			'iglesia_fuera' : up_cere.iglesia_fuera,
			'ceremonia' : up_cere.ceremonia,
			'ramo' : up_cere.ramo,
			'pajecitos' : up_cere.pajecitos,
			'carro_antiguo' : up_cere.carro_antiguo,
			'coros' : up_cere.coros,
			'boutonnieres' : up_cere.boutonnieres,
			'servicio_fotografia' : up_cere.servicio_fotografia
			}	

	return render(request, 'ceremonia_edit.html', context)

def fiesta(request):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	fest = Fiesta.objects.all()
	if not len(fest):
		fest_form = Fiesta_Form(request.POST or None)
		context = {
			'costos' : costos,
			'fest_form' : fest_form
		}

		if fest_form.is_valid():
			form_data = fest_form.cleaned_data
			recordatorios = form_data.get("recordatorios")
			musica = form_data.get("musica")
			tarjetas = form_data.get("tarjetas")
			licores = form_data.get("licores")
			fuera_ciudad = form_data.get("fuera_ciudad")
			flores = form_data.get("flores")
			organizadora = form_data.get("organizadora")

			new_fest = Fiesta.objects.create(recordatorios=recordatorios, musica=musica, tarjetas=tarjetas, 
				licores=licores, fuera_ciudad=fuera_ciudad, flores=flores, organizadora=organizadora)

			calcular_costos()
			return HttpResponseRedirect('fiesta')

		return render(request, 'fiesta.html', context)

	else:
		up_fest = Fiesta.objects.all()[0]
		
		fest_form = Fiesta_Form(request.POST or None, instance=up_fest)
		context = {
			'costos' : costos,
			'fest_form' : fest_form
		}

		if fest_form.is_valid():
			form_data = fest_form.cleaned_data
			up_fest.recordatorios = form_data.get("recordatorios")
			up_fest.musica = form_data.get("musica")
			up_fest.tarjetas = form_data.get("tarjetas")
			up_fest.licores = form_data.get("licores")
			up_fest.fuera_ciudad = form_data.get("fuera_ciudad")
			up_fest.flores = form_data.get("flores")
			up_fest.organizadora = form_data.get("organizadora")
			up_fest.save()
			calcular_costos()
			return HttpResponseRedirect('fiesta')

		context = {
			'costos' : costos,
			'fest_form' : fest_form,
			'recordatorios' : up_fest.recordatorios,
			'musica' : up_fest.musica,
			'tarjetas' : up_fest.tarjetas,
			'licores' : up_fest.licores,
			'fuera_ciudad' : up_fest.fuera_ciudad,
			'flores' : up_fest.flores,
			'organizadora' : up_fest.organizadora
			}

	
	return render(request, 'fiesta_edit.html', context)

def luna_miel(request):
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	luna = Luna_Miel.objects.all()
	
	if not len(luna):
		luna_form = Luna_Miel_Form(request.POST or None)
		context = {
			'costos' : costos,
			'luna_form' : luna_form
		}

		if luna_form.is_valid():
			form_data = luna_form.cleaned_data
			viaje_colombia = form_data.get("viaje_colombia")

			new_luna = Luna_Miel.objects.create(viaje_colombia=viaje_colombia)

			calcular_costos()
			return HttpResponseRedirect('luna_miel')

		return render(request, 'luna_miel.html', context)

	else:
		up_luna = Luna_Miel.objects.all()[0]
		
		luna_form = Luna_Miel_Form(request.POST or None, instance=up_luna)
		context = {
			'costos' : costos,
			'luna_form' : luna_form
		}

		if luna_form.is_valid():
			form_data = luna_form.cleaned_data
			up_luna.viaje_colombia = form_data.get("viaje_colombia")
			up_luna.save()
			calcular_costos()
			return HttpResponseRedirect('luna_miel')

		context = {
			'costos' : costos,
			'luna_form' : luna_form,
			'viaje_colombia' : up_luna.viaje_colombia
			}


	return render(request, 'luna_miel_edit.html', context)

def calcular_costos():
	bodas = Boda.objects.all()
	if bodas:
		costo_min = 0
		costo_max = 0
		boda = Boda.objects.all()[0]
		pareja = Pareja.objects.all()[0]
		personas = boda.personas
		if pareja.curso_pre:
			costo_min += 120000
			costo_max += 120000
		if pareja.argollas:
			costo_min += 500000
			costo_max += 3000000
		if pareja.confirmacion_novia:
			costo_min += 55000
			costo_max += 55000
		if pareja.docs_novia:
			costo_min += 60000
			costo_max += 60000
		if pareja.vestido_novia:
			costo_min += 700000
			costo_max += 2000000
		if pareja.maquillaje_peinado:
			costo_min += 150000
			costo_max += 500000
		if pareja.estetica:
			costo_min += 80000
			costo_max += 80000
		if pareja.confirmacion_novio:
			costo_min += 55000
			costo_max += 55000
		if pareja.docs_novio:
			costo_min += 60000
			costo_max += 60000
		if pareja.vestido_novio:
			costo_min += 350000
			costo_max += 1200000

		ceres = Ceremonia.objects.all()
		if ceres:
			cere = Ceremonia.objects.all()[0]
			#Iglesia
			if cere.tipo == 'Iglesia':
				if cere.iglesia_fuera:
					costo_min += 70000
					costo_max += 150000
				if cere.ceremonia:
					costo_min += 100000
					costo_max += 250000
			#Civil
			if cere.tipo == 'Civil':
				if cere.ceremonia:
					costo_min += 40000
					costo_max += 40000
			#Ambos
			if cere.abogado:
				costo_min += 100000
				costo_max += 100000
			if cere.flores:
				costo_min += 300000
				costo_max += 300000
			if cere.ramo:
				costo_min += 70000
				costo_max += 70000
			if cere.pajecitos:
				costo_min += 150000
				costo_max += 150000
			if cere.carro_antiguo:
				costo_min += 280000
				costo_max += 400000
			if cere.coros:
				costo_min += 150000
				costo_max += 150000
			if cere.boutonnieres:
				costo_min += 100000
				costo_max += 100000
			if cere.servicio_fotografia:
				costo_min += 1000000
				costo_max += 1800000

		fests = Fiesta.objects.all()
		if fests:
			fest = Fiesta.objects.all()[0]
			if fest.recordatorios:
				costo_min += 1500000
				costo_max += 1500000
			if fest.musica == 'Vivo':
				costo_min += 2000000
				costo_max += 5000000
			if fest.musica == 'DJ':
				costo_min += 500000
				costo_max += 2000000
			if fest.tarjetas:
				costo_min += 500000
				costo_max += 1000000
			if fest.licores:
				costo_min += 1500000
				costo_max += 2500000
			if fest.fuera_ciudad:
				costo_min += 600000
				costo_max += 900000
			if fest.flores:
				costo_min += 300000
				costo_max += 300000
			if fest.organizadora:
				costo_min += 1500000
				costo_max += 3000000

		lunas = Luna_Miel.objects.all()
		if lunas:
			luna = Luna_Miel.objects.all()[0]
			if luna.viaje_colombia:
				costo_min += 4000000
				costo_max += 6000000
						
		boda.costo_alto = costo_max
		boda.costo_bajo = costo_min
		boda.save()

def pago(request):
	response_one_dollar= requests.get('http://www.xe.com/es/currencyconverter/convert/?Amount=1&From=USD&To=COP')
	soup_one_dollar = BeautifulSoup(response_one_dollar.content, 'html.parser')
	container_dollar = soup_one_dollar.find('span', 'uccResultAmount')
	one_dollar = container_dollar.contents[0]
	dolar = one_dollar.string.replace(".", "").replace(",", ".")
	bodas = Boda.objects.all()
	if bodas:
		boda = Boda.objects.all()[0]
		costos = "{}$ - {}$".format(boda.costo_bajo, boda.costo_alto)
	else:
		costos = "No hay registro de boda"

	minimo = round(boda.costo_bajo/float(dolar), 2)
	maximo = round(boda.costo_alto/float(dolar) ,2)

	context = {
		'costos' : costos,
		'dolar' : one_dollar,
		'minimo' : minimo,
		'maximo' : maximo
	}

	return render(request, 'pago.html', context)