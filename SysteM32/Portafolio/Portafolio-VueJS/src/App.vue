<script setup>
import NavBar from './components/NavBar.vue';
import DatosPersonales from './components/DatosPersonales.vue';
</script>


<template>
   <header>
      <!--Barra de Naveegacion-->
      <NavBar />
      <!--Componente de Datos Personales-->
      <DatosPersonales />
   </header>
   <main>
      <section id="experiencia"><h2>Experiencia</h2></section>
      <section id="proyectos"><h2>Proyectos</h2></section>
      <section id="habilidades"><h2>Habilidades</h2></section>
      <section id="intereses"><h2>Intereses</h2></section>
   </main>
</template>

<style scoped>

</style>
