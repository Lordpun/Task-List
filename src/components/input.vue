<template>
	<form v-on:submit.prevent="addTask">
		<input type="text" placeholder="Enter new task" autocomplete="false" v-model="taskDescription">
		<button @click="addTask">Add</button>
	</form>
</template>

<script setup>
	import { invoke } from '@tauri-apps/api/core';
	import { ref } from 'vue';
	const taskDescription = ref('');

	async function addTask() {
		if (taskDescription.value == '') {
			return;
		}

		await invoke("addTask", [taskDescription.value]);

		emit("taskModified")
	}
</script>

<style scoped>
	form {
		padding: 0.5rem 0;
	}
</style>