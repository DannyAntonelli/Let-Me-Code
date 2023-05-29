import { createRouter, createWebHistory } from "vue-router";

import Home from "@/views/Home.vue";
import Login from "@/views/Login.vue";
import Profile from "@/views/Profile.vue";
import Register from "@/views/Register.vue";
import Workspace from "@/views/Workspace.vue";
import Explore from "@/views/Explore.vue";
import Following from "@/views/Following.vue";
import Favorites from "@/views/Favorites.vue";
import NotFound from "@/views/NotFound.vue";

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
  {
    path: "/following",
    name: "Following",
    meta: { requiresAuth: true },
    component: Following,
  },
  {
    path: "/favorites",
    name: "Favorites",
    meta: { requiresAuth: true },
    component: Favorites,
  },
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    component: NotFound,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
