import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

import { faGithub, faLinkedinIn } from "@fortawesome/free-brands-svg-icons";
import { faEnvelope, faUser } from "@fortawesome/free-regular-svg-icons";
import {
  faTerminal,
  faLocationDot,
  faPhone,
  faCode,
  faSignature,
  faLock,
  faMagnifyingGlass,
} from "@fortawesome/free-solid-svg-icons";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
// import "mdb-vue-ui-kit/css/mdb.min.css";
router.beforeEach((to, from, next) => {
  document.title = "Let Me Code - " + to.name;

  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);
  const token = localStorage.getItem("token");

  if (requiresAuth && !token) {
    next("/login");
  } else {
    next();
  }
});

library.add(
  faGithub,
  faLinkedinIn,
  faTerminal,
  faEnvelope,
  faLocationDot,
  faPhone,
  faCode,
  faUser,
  faSignature,
  faLock,
  faMagnifyingGlass
);
const app = createApp(App);
// import contextmenu from "v-contextmenu";
// import "v-contextmenu/dist/themes/default.css";
// app.use(contextmenu);
// import PrimeVue from "primevue/config";
// app.use(PrimeVue);
// import "primevue/resources/themes/lara-light-indigo/theme.css";
// import "primevue/resources/primevue.min.css";
app.use(router).component("font-awesome-icon", FontAwesomeIcon).mount("#app");
