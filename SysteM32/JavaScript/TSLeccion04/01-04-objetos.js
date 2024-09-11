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



