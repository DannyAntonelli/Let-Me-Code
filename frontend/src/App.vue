<template>
  <Navbar @logout="removeUserData" :username="username" />
  <router-view @login="updateUsername" :key="$route.path" />
  <FooterComponent />
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import FooterComponent from "@/components/FooterComponent.vue";

export default {
  name: "App",

  components: {
    Navbar,
    FooterComponent,
  },

  data() {
    return {
      username: localStorage.getItem("username") ?? "",
    };
  },

  async created() {
    let theme = localStorage.getItem("theme");
    if (theme === null) {
      localStorage.setItem("theme", "dark");
      theme = "dark";
    }
    document.documentElement.setAttribute("data-bs-theme", theme);
  },

  methods: {
    updateUsername() {
      this.username = localStorage.getItem("username");
    },

    removeUserData() {
      this.username = "";
    },
  },
};
</script>

<style>
.hidden {
  opacity: 0;
  filter: blur(5px);
  transform: translateX(-100%);
  transition: all 0.7s;
}

.show {
  opacity: 1;
  filter: blur(0);
  transform: translateX(0);
}

.form-check-input[type="checkbox"]:checked {
  background-color: var(--bs-purple);
  border-color: var(--bs-purple);
}
</style>
