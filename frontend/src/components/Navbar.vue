<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <font-awesome-icon icon="fa-solid fa-terminal" />
        Let Me Code
      </a>
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
          <li class="nav-item">
            <router-link class="nav-link active" aria-current="page" to="/"
              >Home</router-link
            >
          </li>
          <li class="nav-item">
            <router-link class="nav-link active" to="/">Explore</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link active" :to="profileRoute"
              >Profile</router-link
            >
          </li>
          <li class="nav-item">
            <router-link class="nav-link active" to="/register"
              >Register</router-link
            >
          </li>
          <li class="nav-item">
            <router-link class="nav-link active" to="/login">Login</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link active" to="/" @click="handleLogout"
              >Logout</router-link
            >
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input
            class="form-control me-2"
            type="search"
            placeholder="Search"
            aria-label="Search"
          />
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",

  props: {
    profileRoute: {
      type: String,
      required: true,
    },
  },

  methods: {
    handleLogout() {
      localStorage.removeItem("token");
      localStorage.removeItem("username");
    },
  },
};
</script>
