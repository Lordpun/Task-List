<template>
	<form v-on:submit.prevent="addTask">
		<input type="text" placeholder="Enter new task" autocomplete="false" v-model="taskDescription">
		<button @click="addTask">Add</button>
	</form>
</template>

<script setup>
	import { ref } from 'vue';
	const taskDescription = ref("")

	function addTask() {
		if (taskDescription == "") {
			return "No description"
		}

		const description = {
			description: taskDescription
		}

		fetch("/task/add", {
			method: "POST",
			headers: {
				"Content-Type": "application/json"
			},
			body: JSON.stringify(description)
		})
	}
</script>

<style scoped>
	form {
		padding: 0.5rem 0;
	}
</style>