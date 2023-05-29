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
    @submit.prevent="handleRegister"
  >
    <h2 class="text-center mb-4"><strong>Sign Up</strong></h2>

    <div class="m-3 row">
      <font-awesome-icon
        icon="fa-regular fa-user"
        class="col-1 mt-2"
        size="lg"
      />
      <input
        type="text"
        id="register-username"
        class="form-control col mr-2"
        v-model="username"
        placeholder="Username*"
        required
      />
    </div>

    <div class="m-3 row">
      <font-awesome-icon
        icon="fa-regular fa-envelope"
        class="col-1 mt-2"
        size="lg"
      />
      <input
        type="email"
        id="register-email"
        class="form-control col"
        v-model="email"
        placeholder="Email"
      />
    </div>

    <div class="m-3 row">
      <font-awesome-icon
        icon="fa-solid fa-signature"
        class="col-1 mt-2"
        size="lg"
      />
      <input
        type="text"
        id="register-first-name"
        class="form-control col"
        v-model="firstName"
        placeholder="First Name"
      />
    </div>

    <div class="m-3 row">
      <font-awesome-icon
        icon="fa-solid fa-signature"
        class="col-1 mt-2"
        size="lg"
      />
      <input
        type="text"
        id="register-last-name"
        class="form-control col"
        v-model="lastName"
        placeholder="Last Name"
      />
    </div>

    <div class="m-3 row">
      <font-awesome-icon icon="fa-solid fa-lock" class="col-1 mt-2" size="lg" />
      <input
        type="password"
        id="register-password"
        class="form-control col"
        v-model="password"
        placeholder="Password*"
        required
      />
    </div>

    <div class="m-3 mb-4 row">
      <font-awesome-icon icon="fa-solid fa-lock" class="col-1 mt-2" size="lg" />
      <input
        type="password"
        id="register-password"
        class="form-control col"
        v-model="repeatedPassword"
        placeholder="Confirm Password*"
        required
      />
    </div>

    <div class="form-check form-switch m-3 mb-4 row">
      <input
        class="form-check-input"
        type="checkbox"
        id="toc"
        checked
        required
      />
      <label class="col form-check-label" for="toc">
        I agree to the
        <a href="https://youtu.be/dQw4w9WgXcQ"
          ><strong>Terms and Conditions</strong></a
        >
      </label>
    </div>

    <button
      type="submit"
      class="btn btn-primary btn-lg"
      style="background-color: var(--bs-purple); border-color: var(--bs-purple)"
    >
      Register
    </button>

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
        this.errorMessage = "Passwords do not match";
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
              localStorage.setItem("token", response.token);
              localStorage.setItem("username", this.username);
              this.$emit("login");
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

<style scoped>
a {
  color: var(--bs-purple);
}
</style>
