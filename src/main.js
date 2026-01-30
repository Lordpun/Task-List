import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router';

app.use(router);
createApp(App).mount('#app')
