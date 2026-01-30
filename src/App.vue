<template>
  <header>
    <h1>Task List</h1>
  </header>

  <main>
    <router-view />
  </main>
</template>

<script setup>
  
</script>

<style scoped>
  header {
    border-bottom: 1px solid #ccc;
    margin-bottom: 1rem;
  }

  h1 {
    font-size: 1.75rem;
  }
</style>
