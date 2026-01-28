<template>
	<form v-on:submit.prevent="addTask">
		<input type="text" placeholder="Enter new task" autocomplete="false" v-model="taskDescription">
		<button @click="addTask">Add</button>
	</form>
</template>

<script setup>
	// import { invoke } from '@tauri-apps/api/core';

	// const runPython = async () => {
	  
	// };
</script>

<style scoped>
	form {
		padding: 0.5rem 0;
	}
</style>