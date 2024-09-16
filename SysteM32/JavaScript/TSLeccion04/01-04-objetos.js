let x = 10; //Variable de tipo primitiva
console.log(x.length);
console.log("Tipos primitivos");
//Objeto
let persona = {
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 30,
    nombreCompleto: function(){ //Metodo o funcion en JavaScript
        return this.nombre+' '+this.apellido;
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email,);
console.log(persona.edad);
console.log(persona.nombreCompleto());
console.log("Ejecutando con un objeto");

let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = "Juan";
persona2.direccion = "Salada 14";
persona2.telefono = "542604651804";  //hasta aca
console.log("Creamos un nuevo objeto");
console.log(persona['apellido']);
console.log("usamos el objeto for in");
// for in y accedemos al objeto como si fuera un arreglo
for (propiedad in persona) {
    
    console.log(propiedad);
    console.log(persona[propiedad]);

}
console.log("cambiamos y eliminamos un error");
persona.apellida = "Perez"; // cambiamos dinamicamente el valor del objeto
delete persona.apellida; // Eliminamos el error 
console.log(persona);

//distintas formas de imprimir un objeto
//Número 1: la mas sencilla : concatenar el valor de cada propiedad
console.log("distintas formas de imprimir un objeto: forma 1");
console.log(persona.nombre+", "+persona.apellido);

// numero 2: A través del ciclo for in
console.log("distintas formas de imprimir un objeto: forma 2");

for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}
console.log("distintas formas de imprimir un objeto: forma 3");

// Numero 3: La función Object.values()
let personaArray = Object.values(persona);
console.log(personaArray);

console.log("distintas formas de imprimir un objeto: forma 4");
let personaString = JSON.stringify(persona);
console.log(personaString);