<template>
  <section>
    <div class="priorityChange"> 
      <priority-btn direction="true"></priority-btn>
      <priority-btn direction="false"></priority-btn>
    </div>

  	<div class="priority">
  		<h4>Priority</h4>
  		<p>{{ priority }}</p>
  	</div>

  	<div class="description">
  		<h4>Task</h4>
  		<p>{{ description }}</p>
  	</div>

  	<div class="date">
  		<h4>Date</h4>
  		<p>{{ date }}</p>
  	</div>

  	<div class="close">
  		<a>X</a>
  	</div>
  </section>
</template>

<script setup>
  import priorityBtn from "./priorityButton.vue";

  const props = defineProps({
    priority: String,
    description: String,
    date: String
  });
</script>
  
<style scoped>
  section {
    display: flex;
    padding: 0 0.5rem;
  }

  section div {
    border: 1px solid #ccc;
    font-size: 1rem;
    padding: 0 0.5rem;
  }

  .priorityChange {
    flex-grow: 0.25;
    padding: 0;
  }

  .priority {
    felx-grow: 0.5;
    text-align: center;
  }

  .description {
    flex-grow: 2;
  }

  .date {
    flex-grow: 0.5;
    text-align: center;
  }

  .status {
   flex-grow: 0.25;
   text-align: center;
  } 
</style>
