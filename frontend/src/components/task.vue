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

  	<div class="status">
  		<h4>Complete</h4>
  		<input type="checkbox">
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
    flex-direction: row;
    padding: 0 0.5rem;
  }

  section div {
    border: 1px solid black;
    font-size: 1rem;
    /*padding: 0 2rem;*/
  }

  .priorityChange {
    flex-grow: 1;
  }

  .priority {
    felx-grow: 2;
    text-align: center;
  }

  .description {
    flex-grow: 4;
  }

  .date {
    flex-grow: 1;
    text-align: center;
  }

  .status {
   flex-grow: 1;
   text-align: center;
  } 
</style>
