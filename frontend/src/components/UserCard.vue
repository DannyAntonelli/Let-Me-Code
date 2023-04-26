<template>
  <div class="card">
    <div class="card-body">
      <router-link :to="profileUrl"
        ><h5 class="card-title" style="font-size: large">
          <font-awesome-icon icon="fa-regular fa-user" size="s" />
          <strong class="m-2">@{{ user.username }} {{ fullName }} </strong>
        </h5></router-link
      >
      <h6 class="card-subtitle mb-2 text-muted">
        Member since: Tue Apr 25 2023
      </h6>
      <p class="card-text mb-0">
        Number of public projects: {{ user.number_of_public_projects }}
      </p>
      <p class="card-text">
        Number of public contributions:
        {{ user.number_of_shared_public_projects }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserCard",

  props: {
    user: {
      type: Object,
      required: true,
    },
  },

  computed: {
    fullName() {
      let fullName = `${this.user.first_name} ${this.user.last_name}`.trim();
      return fullName !== "" ? `(${fullName})` : "";
    },

    profileUrl() {
      return `/profile/${this.user.username}`;
    },
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: inherit;
}
</style>
