<script setup>
const title = 'Juan Perez';
const descripcion = 'Tecnico Universitario en Programacion - UTN';
const residencia = 'San Rafael, Mendoza, Argentina';
const presentacion = 'Hola, Bienvenido a mi portafolio de proyectos. Soy un desarrollador web con experiencia en el desarrollo de aploicaciones web y moviles';
const redesSociales = [
    {id: 1, name:'linkedin', src: '', url:''},
    {id: 2, name:'Instagram', src: '', url:''},
    {id: 3, name:'gitHub', src: '', url:''},
    {id: 4, name:'curriculum', src: '', url:''},
];
const telefono = '+54 9 2604-474849';
</script>

<template>
<section class="datos personales">
    <div class="card">
        <h1>{{ title }}</h1>
        <h2>{{ descripcion }}</h2>
        <p>{{ presentacion }}</p>
        <ul class="container-listas">
           <li v-for="red in redesSociales" :key="red.id">
            <a href="red.url"><img class="icon-residencial" src="" width="35rem" alt="red.name"></a>
           </li>
        </ul>
        <h3>Mi Telefono personal: {{ telefono }}</h3>
        <h4>{{ residencia }}</h4>
    </div>
</section>
</template>

<style scoped>
 h1{
    font-size: 2.5rem;
 }
 p{
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1rem;
 }

 .card {
    background-color: rgb(28, 41, 52);
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
    text-align: center;
    color: azure;
 }

 .container-lista {
    display: flex;
    justify-content: center;
    list-style: none;
    padding: 0;
    margin: 0;
    text-align: center;
 }

 .icon-redsocial {
    align-items: center;
    background-color: aliceblue;
    border-radius: 50%;
    padding: 2px;
    margin: 5px;
    box-shadow: 0 0 5px rgb(95, 124, 205, 0.934);
 }

 .icon-redsocial:hover {
    background-color: rgb(28, 41, 52);
    box-shadow: 0 0 5px rgb(251, 249, 249, 0.934);
 }

 h3{
    font-size: 1.2rem;
    font-weight: 600;
 }
</style>