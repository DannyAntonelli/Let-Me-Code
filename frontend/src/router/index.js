import { createRouter, createWebHistory } from "vue-router";

import Home from "@/views/Home.vue";
import Login from "@/views/Login.vue";
import Profile from "@/views/Profile.vue";
import Register from "@/views/Register.vue";
import Workspace from "@/views/Workspace.vue";
import Explore from "@/views/Explore.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/explore",
    name: "Explore",
    component: Explore,
    meta: { requiresAuth: true },
  },
  {
    path: "/profile/:username",
    name: "Profile",
    component: Profile,
    meta: { requiresAuth: true },
  },
  {
    path: "/project/:id",
    name: "Project",
    component: Workspace,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
