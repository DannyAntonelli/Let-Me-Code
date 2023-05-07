<template>
  <Navbar @logout="removeUserData" :isLoggedIn="isLoggedIn" />
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
      isLoggedIn: localStorage.getItem("token") ? true : false,
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
      this.isLoggedIn = true;
    },

    removeUserData() {
      this.isLoggedIn = false;
    },
  },
};
</script>
