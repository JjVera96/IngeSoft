function validar() {
	var nombre_novia;
	nombre_novia = document.getElementById("nombre_novia").value;

	if (nombre_novia == "Albert") {
		alert("Perrito no puede estar vacio");
		return false;
	}

}