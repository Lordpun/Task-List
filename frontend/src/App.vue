<template>
  <header>
    <h1>Task List</h1>
  </header>

  <main>
    <section>
      <h4>Your Current Tasks</h4>
    </section>

    <section class="taskBody">
      <task></task>
    </section>
  </main>
</template>

<script setup>
	import task from "./components/task.vue"
</script>

<style scoped>
  header {
    border-bottom: 1px solid #ccc;
    margin-bottom: 1rem;
  }

  h1 {
    font-size: 1.75rem;
  }

  main section {
    border: 1px solid #ccc;
    width: 90%;
    margin: 0 auto;
    text-align: center;
  }
</style>
