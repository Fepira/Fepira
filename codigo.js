//ARRAYS

//Arrays: cómo declararlas e inicializarlas

let arrays = ["felix", 23, "Santiago"];
let frutas = ["banana", "mansana", "pera"];
// posiciones:   0          1        2
// si no existe la posición, me devolverá un undefined, 
// pues todas las posiciones estan
// declaradas, pero no estan definidas
document.write(frutas[1])

//Arrays asociativos

let pc = {
	nombre: "Pc de félix",
	procesador: "Intel core I7",
	ram : "16 GB",
	espacio: "1TB"
};

let nombre = pc["nombre"];
let procesador = pc["procesador"];
let ram = pc["ram"];
let espacio = pc["espacio"];

let frase = `El ${nombre} tiene un procesador <br>
${procesador}, una ram de ${ram} <br> y tiene un espacio de ${espacio}`;
document.write(frase)


// BUCLES

//While

let numero = 0

while (numero < 6){
	numero++;

	document.write(numero + "<br>")

};

//do while

do {
	numero++;

	document.write(numero + "<br>")
};

while (numero <= 6)

// break


while(numero < 1000){
	numero++;
	document.write(numero);
	if (numero==10){
		break;
	};
};

// for

for (let i = 0; i < 6; i++){
	document.write(i + "<br>")

}