<template>
  <section>
  	<div class="priority">
  		<h4>Priority</h4>
  		<p>{{ priority }}</p>
  	</div>

  	<div class="description">
  		<h4>Task</h4>
  		<p>{{ description }}</p>
  	</div>

  	<div class="date">
  		<h4>Date Added</h4>
  		<p>{{ date }}</p>
  	</div>

  	<div class="status">
  		<h4>Complete</h4>
  		<input type="checkbox">
  	</div>
  </section>
</template>

<script setup></script>

<style scoped></style>
