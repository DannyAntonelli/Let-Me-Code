<template>
  <Navbar :profileRoute="profileRoute" />
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
    },
  },
};
</script>
