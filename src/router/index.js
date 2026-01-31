import { createRouter, createWebHistory } from 'vue-router';
import noFile from '../pages/noFile.vue';
import fileLoaded from '../pages/fileLoaded.vue';

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