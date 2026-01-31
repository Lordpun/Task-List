<template>
	<a class="priorityChangeBtn">
		<h4 v-if="direction">↑</h4>
		<h4 v-else>↓</h4>
	</a>
</template>

<script setup>
	const props = defineProps({
		// True for up, false for down
		direction: Boolean
	})
</script>

<style scoped>
	a {
		display: block;
		text-align: center;
		width: 100%;
		height: 50%;
		padding: 0;
		margin: 0;
		cursor: pointer;
		background-color: #ddd;
		display: grid;
    place-items: center;
	}

	a:hover {
		background-color: #bbb;
	}

	a:active {
	</style>	background-color: #eee;
	}
