import { createRouter, createWebHistory } from 'vue-router';
import noFile from '../views/HomeView.vue';
import fileLoaded from '../views/AboutView.vue';

const routes = [
  {
    path: '/',
    name: 'noFile',
    component: noFile
  },
  {
    path: '/fileLoaded',
    name: 'fileLoaded',
    component: fileLoaded
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;