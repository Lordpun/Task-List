<template>
	<section>
		<h4>No file selected</h4>
		<p>Select one here:</p>
		<input type="file" @change="getFile" acecept=".json">
	</section>
</template>

<script setup>
	import { useJsonStore } from '@/stores/jsonStore'
	
	function getFile() {
		const file = this.files[0];

		const reader = new FileReader();
		reader.onload = (e) => {
			console.log("Not implemented yet");
		} catch (error) {
			console.log("Invalid JSON file");
		}
	}
</script>