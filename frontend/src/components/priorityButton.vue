<template>
	<button class="priorityChangeBtn">
		<h4 v-if="direction">↑</h4>
		<h4 v-else>↓</h4>

	</button>
</template>

<script setup>
	const props = defineProps({
		// True for up, false for down
		direction: Boolean
	})
</script>

<style scoped>
	button {
		width: 100%;
		height: 25%;
		padding: 0;
		margin: 0;
	}
</style>