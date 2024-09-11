<template>
          <nav class = "navbar">
         <div class="navbar-menu">
            <ul>
                <a v-for="nav in navegacion" :key="nav.nombre" href="nav.enlace" class="nav-item">{{ nav.nombre }}</a>
            </ul>
         </div>
      </nav>
</template>

<script setup>
import { ref } from 'vue';
const navegacion = ref([
    {id:1, nombre: 'Educacion', enlace: '#educacion'},
    {id:2, nombre: 'Experiencia', enlace: '#experiencia'},
    {id:3, nombre: 'Proyectos', enlace: '#proyectos'},
    {id:4, nombre: 'Habilidades', enlace: '#habilidades'}
]);
</script>

<style scoped>
.navbar{
   background-color:var(--vt-c-indigo);
   color: #fff;
   padding: 0.5rem 1rem;
   align-items: center;
}
.navbar-item{
   color: #fff;
   text-decoration: none;
   margin-right: 1rem;
}
.navbar-menu{
   display: flex;
   justify-content: flex-end;
}
.nav-list{
   list-style: none;
}

a{
    border:1px solid;
    border-color: hsla(160, 100%, 37%, 0.2);
    border-radius: 5px;
    text-decoration: none;
    transition: 0.4s;
    padding: 5px;
}
a:hover{
    background-color: hsla(160, 100%, 37%, 0.2);;
}
</style>