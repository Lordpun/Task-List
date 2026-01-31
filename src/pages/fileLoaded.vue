<template>
  <section class="pageBody">
    <h3>{{ store.fileName }}</h3>
    <h4>Your Current Tasks</h4>

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
  </section>
</template>

<script setup>
  import task from "../components/task.vue"
  import inputField from "../components/input.vue"
  import { invoke } from '@tauri-apps/api/core';
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import { useJsonStore } from '@/stores/jsonStore'

  const tasksLoaded = ref([])
  const tasksExist = ref(true)

  const store = useJsonStore();

  function displayTasks() {
    taskData = store.uploadedData;
    if (taskData) tasksLoaded.value = taskData;

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
    margin: 2rem auto;
    padding: 2rem;
    padding-bottom: 0;
    text-align: center;
  }

  .taskInput {
    padding: 0;
  }
</style>