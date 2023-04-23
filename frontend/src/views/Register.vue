<template>
  <form @submit.prevent="handleRegister">
    <div class="form-outline mb-4">
      <input
        type="text"
        id="register-username"
        class="form-control"
        v-model="username"
        required
      />
      <label class="form-label" for="register-username">Username</label>
    </div>

    <div class="form-outline mb-4">
      <input
        type="email"
        id="register-email"
        class="form-control"
        v-model="email"
        required
      />
      <label class="form-label" for="register-email">Email</label>
    </div>

    <div class="form-outline mb-4">
      <input
        type="text"
        id="register-first-name"
        class="form-control"
        v-model="firstName"
        required
      />
      <label class="form-label" for="register-first-name">First Name</label>
    </div>

    <div class="form-outline mb-4">
      <input
        type="text"
        id="register-last-name"
        class="form-control"
        v-model="lastName"
        required
      />
      <label class="form-label" for="register-last-name">Last Name</label>
    </div>

    <div class="form-outline mb-4">
      <input
        type="password"
        id="register-password"
        class="form-control"
        v-model="password"
        required
      />
      <label class="form-label" for="register-password">Password</label>
    </div>

    <button type="submit" class="btn btn-primary btn-block mb-4">
      Register
    </button>

    <div class="text-center">
      <p>
        Already have an account? <router-link to="/login">Login</router-link>
      </p>
    </div>
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
    };
  },

  methods: {
    handleRegister() {
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
              this.$router.push("/");
            })
            .catch((error) => {
              console.log(error);
            });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  emits: {
    login: null,
  },
};
</script>
