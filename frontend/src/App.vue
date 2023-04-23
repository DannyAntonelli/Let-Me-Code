<template>
  <Navbar :profileRoute="profileRoute" />
  <router-view @login="updateUsername" :key="$route.path" />
</template>

<script>
import Navbar from "@/components/Navbar.vue";

export default {
  name: "App",

  data() {
    return {
      profileRoute: "/profile/" + localStorage.getItem("username"),
    };
  },

  components: {
    Navbar,
  },

  methods: {
    updateUsername(username) {
      console.log("Updating username to " + username);
      localStorage.setItem("username", username);
      this.profileRoute = "/profile/" + username;
    },
  },
};
</script>
