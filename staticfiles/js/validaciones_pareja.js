function validar() {
	var nombre_novia, apellido_novia, nombre_novio, apellido_novio, fecha_hora, personas;

	nombre_novia = document.getElementById("nombre_novia").value;
	apellido_novia = document.getElementById("apellido_novia").value;
	nombre_novio = document.getElementById("nombre_novio").value;
	apellido_novio = document.getElementById("apellido_novio").value;
	fecha_hora = document.getElementById("fecha_hora").value;
	personas = document.getElementById("personas").value;

	if (nombre_novia == "" || apellido_novia == "" || nombre_novio == "" || apellido_novio == "" || fecha_hora == "" || personas == "" ) {
		alert("Todos los campos son obligatorios");
		return false;
	}

	if (nombre_novia.length>50) {
		alert("Nombre de la Novia es demasiado largo, maximo 50 caracteres");
		return false;	
	}
	
	if (nombre_novio.length>50) {
		alert("Nombre del Novio es demasiado largo, maximo 50 caracteres");
		return false;	
	}

	if (apellido_novia.length>50) {
		alert("Apellido de la Novia es demasiado largo, maximo 50 caracteres");
		return false;	
	}

	if (apellido_novio.length>50) {
		alert("Apellido del Novio es demasiado largo, maximo 50 caracteres");
		return false;	
	}

	if (isNaN(personas)) {
		alert("El cantidad de personas ingresado no es un numero");
		return false;
	}

	var exp = /^[a-zA-Z ]*$/;

	if (!exp.test(nombre_novia)) {
		alert("Nombre de la Novia solo puede tener letras");
		return false;
	}

	if (!exp.test(nombre_novia)) {
		alert("Nombre de la Novia solo puede tener letras");
		return false;
	}

	if (!exp.test(nombre_novio)) {
		alert("Nombre del Novio solo puede tener letras");
		return false;
	}

	if (!exp.test(apellido_novia)) {
		alert("Apellido de la Novia solo puede tener letras");
		return false;
	}

	if (!exp.test(apellido_novio)) {
		alert("Apellido del Novio solo puede tener letras");
		return false;
	}
}

