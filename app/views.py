# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Invitado, Sala, Regalo, Mesa, Camarero, Pareja, Boda, Ceremonia, Fiesta, Luna_Miel
from .forms import Invitado_Form, Sala_Form, Regalo_Form, Mesa_Form, Camarero_Form, Boda_Form, Pareja_Form, Ceremonia_Form, Fiesta_Form, Luna_Miel_Form


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
		direccion = form_data.get("direccion")
		invitado = Invitado.objects.create(nombre=nombre, apellido=apellido, direccion=direccion)
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
		url = "/app/logistica/listar_regalos/{}".format(id_user)
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

def pareja(request):
	boda = Boda.objects.all()
	
	if not len(boda):
		boda_form = Boda_Form(request.POST or None)
		pareja_form = Pareja_Form(request.POST or None)
		context = {
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

			return HttpResponseRedirect('pareja')

		return render(request, 'pareja.html', context)

	else:
		up_pareja = Pareja.objects.all()[0]
		up_boda = Boda.objects.all()[0]
		
		boda_form = Boda_Form(request.POST or None, instance=up_boda)
		pareja_form = Pareja_Form(request.POST or None, instance=up_pareja)
		context = {
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

		context = {
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
	cere = Ceremonia.objects.all()
	
	if not len(cere):
		print("Hola")
		cere_form = Ceremonia_Form(request.POST or None)
		context = {
			'cere_form' : cere_form
		}

		if cere_form.is_valid():
			print("Valido")
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

			return HttpResponseRedirect('ceremonia')

		return render(request, 'ceremonia.html', context)

	else:
		print("Perro")
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

		context = {
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
	fest = Fiesta.objects.all()
	print(fest)
	if not len(fest):
		fest_form = Fiesta_Form(request.POST or None)
		context = {
			'fest_form' : fest_form
		}

		if fest_form.is_valid():
			form_data = fest_form.cleaned_data
			recordatorios = form_data.get("recordatorios")
			musiva_vivo = form_data.get("musiva_vivo")
			tarjetas = form_data.get("tarjetas")
			licores = form_data.get("licores")
			fuera_ciudad = form_data.get("fuera_ciudad")
			flores = form_data.get("flores")

			new_fest = Fiesta.objects.create(recordatorios=recordatorios, musiva_vivo=musiva_vivo, tarjetas=tarjetas, 
				licores=licores, fuera_ciudad=fuera_ciudad, flores=flores)

			return HttpResponseRedirect('fiesta')

		return render(request, 'fiesta.html', context)

	else:
		up_fest = Fiesta.objects.all()[0]
		
		fest_form = Fiesta_Form(request.POST or None, instance=up_fest)
		context = {
			'fest_form' : fest_form
		}

		if fest_form.is_valid():
			form_data = fest_form.cleaned_data
			up_fest.recordatorios = form_data.get("recordatorios")
			up_fest.musiva_vivo = form_data.get("musiva_vivo")
			up_fest.tarjetas = form_data.get("tarjetas")
			up_fest.licores = form_data.get("licores")
			up_fest.fuera_ciudad = form_data.get("fuera_ciudad")
			up_fest.flores = form_data.get("flores")
			up_fest.save()

		context = {
			'fest_form' : fest_form,
			'recordatorios' : up_fest.recordatorios,
			'musiva_vivo' : up_fest.musiva_vivo,
			'tarjetas' : up_fest.tarjetas,
			'licores' : up_fest.licores,
			'fuera_ciudad' : up_fest.fuera_ciudad,
			'flores' : up_fest.flores
			}

	return render(request, 'fiesta_edit.html', context)

def luna_miel(request):
	luna = Luna_Miel.objects.all()
	
	if not len(luna):
		luna_form = Luna_Miel_Form(request.POST or None)
		context = {
			'luna_form' : luna_form
		}

		if luna_form.is_valid():
			form_data = luna_form.cleaned_data
			viaje_colombia = form_data.get("viaje_colombia")

			new_luna = Luna_Miel.objects.create(viaje_colombia=viaje_colombia)

			return HttpResponseRedirect('luna_miel')

		return render(request, 'luna_miel.html', context)

	else:
		up_luna = Luna_Miel.objects.all()[0]
		
		luna_form = Luna_Miel_Form(request.POST or None, instance=up_luna)
		context = {
			'luna_form' : luna_form
		}

		if luna_form.is_valid():
			form_data = luna_form.cleaned_data
			up_luna.viaje_colombia = form_data.get("viaje_colombia")
			up_luna.save()

		context = {
			'luna_form' : luna_form,
			'viaje_colombia' : up_luna.viaje_colombia
			}
	return render(request, 'luna_miel_edit.html', context)

