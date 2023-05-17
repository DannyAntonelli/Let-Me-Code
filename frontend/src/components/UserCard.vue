<template>
  <div class="card hidden">
    <div class="card-body">
      <router-link :to="profileUrl"
        ><h5 class="card-title" style="font-size: large">
          <img
            :src="avatarUrl"
            class="rounded-circle"
            alt="avatar"
            style="width: 2rem; height: 2rem"
          />
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
import MD5 from "crypto-js/md5";

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

    avatarUrl() {
      let hash = MD5(this.user.username).toString();
      return `https://www.gravatar.com/avatar/${hash}?d=identicon`;
    },
  },

  async mounted() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          observer.unobserve(entry.target);
          entry.target.classList.add("show");
        }
      });
    });

    document
      .querySelectorAll(".hidden")
      .forEach((element) => observer.observe(element));
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: inherit;
}
</style>
