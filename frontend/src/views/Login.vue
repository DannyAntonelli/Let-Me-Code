<template>
  <div
    class="alert alert-danger alert-dismissible fade show"
    role="alert"
    v-if="errorMessage"
  >
    <strong>Error during login:</strong> {{ errorMessage }}
  </div>

  <form
    class="text-center"
    style="max-width: 500px; margin: auto"
    @submit.prevent="handleLogin"
  >
    <h2 class="text-center mb-4"><strong>Sign In</strong></h2>

    <div class="m-3 row">
      <font-awesome-icon
        icon="fa-regular fa-user"
        class="col-1 mt-2"
        size="lg"
      />
      <input
        type="text"
        id="login-username"
        class="form-control col mr-2"
        v-model="username"
        placeholder="Username"
        required
      />
    </div>

    <div class="m-3 mb-4 row">
      <font-awesome-icon icon="fa-solid fa-lock" class="col-1 mt-2" size="lg" />
      <input
        type="password"
        id="login-password"
        class="form-control col"
        v-model="password"
        placeholder="Password"
        required
      />
    </div>

    <button type="submit" class="btn btn-dark btn-lg">Log In</button>

    <p class="mt-3">
      Don't have an account?
      <router-link to="/register"><strong>Register</strong></router-link>
    </p>
  </form>
</template>

<script>
import { login } from "@/api/user.js";

export default {
  name: "Login",

  data() {
    return {
      username: "",
      password: "",
      errorMessage: "",
    };
  },

  methods: {
    handleLogin() {
      login(this.username, this.password)
        .then((response) => {
          console.log(response);
          localStorage.setItem("token", response.token);
          this.$emit("login", this.username);
          this.$router.push("/explore");
        })
        .catch((error) => {
          console.log(error);
          this.errorMessage = error.message;
        });
    },
  },

  emits: {
    login: null,
  },
};
</script>
