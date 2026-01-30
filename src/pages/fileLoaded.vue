<template>
  <section>
      <h4>Your Current Tasks</h4>
    </section>

    <ul v-if="tasksExist" class="taskBody">
      <task
      v-for="(task, index) in tasksLoaded"
      :key="index"
      v-bind="task"
       />
    </ul>

    <ul v-else>
      <h4>No tasks exist</h4>
    </ul>

    <section class="taskInput">
      <inputField />
    </section>
</template>

<script setup>
  import task from "./components/task.vue"
  import inputField from "./components/input.vue"
  import { invoke } from '@tauri-apps/api/core';
  import { ref, onMounted } from 'vue';

  const tasksLoaded = ref([])
  const tasksExist = ref(true)

  async function displayTasks() {
    const taskJson = await callFunction("get_tasks");
    tasksLoaded.value = JSON.parse(taskJson);

    if ( tasksLoaded.value.length <= 0 ) { tasksExist.value = false; }
    else { tasksExist.value = true; }
  }

  onMounted(() => {
    displayTasks();
  });
</script>

<style scoped>
  section {
    border: 1px solid #ccc;
    width: 90%;
    margin: 0 auto;
    text-align: center;
  }
</style>