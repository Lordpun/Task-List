<template>
  <section>
    <div class="priorityChange"> 
      <priority-btn></priority-btn>
      <priority-btn></priority-btn>
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
  import priorityBtn from "/priorityChangeBtn.vue";

  const props = defineProps({
    priority: String,
    description: String,
    date: String
  });
</script>
  
<style scoped>
  section {
    display: inline;
    padding: 0;
  }

  section div {
    display: inline-block;
  }

  .priorityChange {
    width: 10%;  
  }
  .priority {
    width: 10%;
  }

  .description {
    width: 60%;
  }

  .date {
    width: 20%;
  }

  .status {
   width: 20%; 
  } 
</style>
