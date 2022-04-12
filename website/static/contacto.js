var email = document.getElementById("e-mail");
var direccion = document.getElementById("direccion");
var ciudad = document.getElementById("ciudad");
var comunidad = document.getElementById("comunidad");
var codigoPostal = document.getElementById("codigo-postal");
var proteccionConfirmacion = document.getElementById("proteccion-confirmacion");

var datos = {
	"e-mail": email,
	"direccion": direccion,
	"ciudad" : ciudad,
	"comunidad" : comunidad,
	"codigo-postal" : codigoPostal,
	"proteccion-confirmacion" : proteccionConfirmacion
};

var datosJSON = JSON.parse(datos);
writeFileSync('contact.json', datosJSON, finished);

document.getElementById("textoJson").innerHTML = 
"e-mail:" + obj.e-mail +
"ciudad: " + obj.ciudad;
