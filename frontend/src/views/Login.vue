<template>
  <div
    class="alert alert-danger alert-dismissible fade show"
    role="alert"
    v-if="errorMessage"
  >
    <strong>Error during login:</strong> {{ errorMessage }}
  </div>

  <form
    class="text-center mt-5"
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
        :type="showPassword ? 'text' : 'password'"
        id="login-password"
        class="form-control col"
        v-model="password"
        placeholder="Password"
        required
      />
      <font-awesome-icon
        :icon="`fa-solid fa-eye${showPassword ? '-slash' : ''}`"
        class="col-1 mt-2"
        style="cursor: pointer"
        @click="showPassword = !showPassword"
      />
    </div>

    <button
      type="submit"
      class="btn btn-primary btn-lg mt-2"
      style="background-color: var(--bs-purple); border-color: var(--bs-purple)"
    >
      Log In
    </button>

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
      showPassword: false,
    };
  },

  methods: {
    handleLogin() {
      login(this.username, this.password)
        .then((response) => {
          localStorage.setItem("token", response.token);
          localStorage.setItem("username", this.username);
          this.$emit("login");
          this.$router.push("/explore");
        })
        .catch((error) => {
          console.log(error);
          this.errorMessage = error.message;
        });
    },
  },
};
</script>

<style scoped>
a {
  color: var(--bs-purple);
}
</style>
