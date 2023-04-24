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
    style="max-width: 450px; margin: auto"
    @submit.prevent="handleRegister"
  >
    <h2 class="text-center mb-4"><strong>Sign Up</strong></h2>

    <div class="mb-3">
      <input
        type="text"
        id="register-username"
        class="form-control"
        v-model="username"
        placeholder="Username*"
        required
      />
    </div>

    <div class="mb-3">
      <input
        type="email"
        id="register-email"
        class="form-control"
        v-model="email"
        placeholder="Email"
      />
    </div>

    <div class="mb-3">
      <input
        type="text"
        id="register-first-name"
        class="form-control"
        v-model="firstName"
        placeholder="First Name"
      />
    </div>

    <div class="mb-3">
      <input
        type="text"
        id="register-last-name"
        class="form-control"
        v-model="lastName"
        placeholder="Last Name"
      />
    </div>

    <div class="mb-3">
      <input
        type="password"
        id="register-password"
        class="form-control"
        v-model="password"
        placeholder="Password*"
        required
      />
    </div>

    <div class="mb-4">
      <input
        type="password"
        id="register-password"
        class="form-control"
        v-model="repeatedPassword"
        placeholder="Repeat Password*"
        required
      />
    </div>

    <button type="submit" class="btn btn-primary btn-lg">Register</button>

    <p class="mt-3">
      Already have an account?
      <router-link to="/login"><strong>Login here</strong></router-link>
    </p>
  </form>
</template>

<script>
import { register, login } from "@/api/user.js";

export default {
  name: "Register",

  data() {
    return {
      username: "",
      email: "",
      firstName: "",
      lastName: "",
      password: "",
      repeatedPassword: "",
      errorMessage: "",
    };
  },

  methods: {
    handleRegister() {
      if (this.password !== this.repeatedPassword) {
        alert("Passwords do not match!");
        return;
      }
      register(
        this.username,
        this.email,
        this.firstName,
        this.lastName,
        this.password
      )
        .then(() => {
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
