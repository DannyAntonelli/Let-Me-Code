import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

import {
  faEnvelope,
  faUser,
  faStar as faStarRegular,
  faFolder,
  faFolderOpen,
  faFloppyDisk,
  faFile,
  faCircleQuestion,
} from "@fortawesome/free-regular-svg-icons";

import {
  faTerminal,
  faLocationDot,
  faPhone,
  faCode,
  faSignature,
  faLock,
  faMagnifyingGlass,
  faStar as fasStarSolid,
  faCircleHalfStroke,
  faGear,
  faCircle,
  faPlus,
  faPenToSquare,
  faUserPlus,
  faUserMinus,
  faTrash,
} from "@fortawesome/free-solid-svg-icons";

import {
  faGithub,
  faLinkedinIn,
  faPython,
  faJsSquare,
  faPhp,
  faCss3,
  faHtml5,
  faJava,
  faGolang,
  faRust,
} from "@fortawesome/free-brands-svg-icons";

import "bootstrap/dist/css/bootstrap.min.css";

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
  faMagnifyingGlass,
  faStarRegular,
  fasStarSolid,
  faCircleHalfStroke,
  faGear,
  faCircle,
  faPlus,
  faPenToSquare,
  faUserPlus,
  faUserMinus,
  faPlus,
  faFolder,
  faFolderOpen,
  faFloppyDisk,
  faFile,
  faCircleQuestion,
  faTrash,
  faPython,
  faJsSquare,
  faPhp,
  faCss3,
  faHtml5,
  faJava,
  faGolang,
  faRust
);
const app = createApp(App);
app.use(router).component("font-awesome-icon", FontAwesomeIcon).mount("#app");
