<template>
	<section>
		<h4>No file selected</h4>
		<p>To get started, make an empty JSON file</p>
		<p>Select one here:</p>
		<input type="file" @change="getFile" acecept=".json">
	</section>
</template>

<script setup>
	import { useJsonStore } from '@/stores/jsonStore'
	import { useRouter } from 'vue-router'

	const store = useJsonStore();
	const router = useRouter();

	function getFile(event) {
		const file = event.target.files[0];

		if (!file) return;

		const reader = new FileReader();
		reader.onload = (e) => {
			const result = e.target.result.trim();
			try {
				if (result === "") {
					store.setJsonData({}, file.name);
				} else {
					const jsonContent = JSON.parse(e.target.result);
					store.setJsonData(jsonContent, file.name);
				}
				router.push("/fileLoaded")
			} catch (error) {
				console.error("Invalid JSON file:", error);
			}
		}

		reader.readAsText(file);
	}
</script>

<style scoped>
	section {
		text-align: center;	
		border: 1px solid #ccc;
		width: 80%;
		margin: 2rem auto;
		padding: 2rem;
	}
</style>