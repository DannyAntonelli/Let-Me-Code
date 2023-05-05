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
