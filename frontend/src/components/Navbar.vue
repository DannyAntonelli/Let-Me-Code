<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/">
        <font-awesome-icon icon="fa-solid fa-terminal" />
        <strong> Let Me Code </strong>
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item" v-if="!isLoggedIn">
            <router-link class="nav-link active" aria-current="page" to="/"
              >Home</router-link
            >
          </li>
          <li class="nav-item" v-if="isLoggedIn">
            <router-link class="nav-link active" to="/explore"
              >Explore</router-link
            >
          </li>
          <li class="nav-item" v-if="isLoggedIn">
            <router-link class="nav-link active" :to="profileRoute"
              >Profile</router-link
            >
          </li>
          <li class="nav-item" v-if="isLoggedIn">
            <router-link
              class="nav-link active"
              to="/favorites"
              :username="username"
              >Favorites</router-link
            >
          </li>
          <li class="nav-item" v-if="!isLoggedIn">
            <router-link class="nav-link active" to="/register"
              >Register</router-link
            >
          </li>
          <li class="nav-item" v-if="!isLoggedIn">
            <router-link class="nav-link active" to="/login">Login</router-link>
          </li>
          <li class="nav-item" v-if="isLoggedIn">
            <router-link class="nav-link active" to="/" @click="handleLogout"
              >Logout</router-link
            >
          </li>
          <li>
            <a @click="toggleTheme">
              <font-awesome-icon
                icon="fa-solid fa-circle-half-stroke"
                class="mt-3 ms-2"
              />
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",

  props: {
    isLoggedIn: {
      type: Boolean,
      required: true,
    },
  },

  methods: {
    handleLogout() {
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      this.$emit("logout");
    },

    toggleTheme() {
      let theme = localStorage.getItem("theme");
      if (theme === "dark") {
        theme = "light";
      } else {
        theme = "dark";
      }
      localStorage.setItem("theme", theme);
      document.documentElement.setAttribute("data-bs-theme", theme);
    },
  },

  computed: {
    username() {
      return localStorage.getItem("username");
    },

    profileRoute() {
      return "/profile/" + this.username;
    },
  },
};
</script>
