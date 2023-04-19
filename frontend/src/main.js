import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'


router.beforeEach((to, from, next) => {
    const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
    const token = localStorage.getItem('token');

    if (requiresAuth && !token) {
        next('/login');
    }
    else {
        next();
    }
})


createApp(App).use(router).mount('#app')
