<template>
  <Navbar
    :profileRoute="profileRoute"
    :isLoggedIn="isLoggedIn"
    @logout="removeUserData"
  />
  <router-view @login="updateUsername" :key="$route.path" />
  <FooterComponent />
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import FooterComponent from "@/components/FooterComponent.vue";

export default {
  name: "App",

  data() {
    return {
      profileRoute: "/profile/" + localStorage.getItem("username"),
      isLoggedIn: localStorage.getItem("token") ? true : false,
    };
  },

  components: {
    Navbar,
    FooterComponent,
  },

  methods: {
    updateUsername(username) {
      localStorage.setItem("username", username);
      this.profileRoute = "/profile/" + username;
      this.isLoggedIn = true;
    },

    removeUserData() {
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      this.isLoggedIn = false;
    },
  },
};
</script>
