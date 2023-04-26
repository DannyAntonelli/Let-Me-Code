<template>
  <div class="row height d-flex justify-content-center align-items-center mt-4">
    <div class="col-md-4">
      <form class="input-group mb-3 p-2" @submit.prevent="search">
        <span class="input-group-text">
          <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
        </span>
        <input
          type="text"
          class="form-control"
          placeholder="Search for a username or project name"
          v-model="query"
        />
      </form>
    </div>
  </div>

  <h3 class="mt-5 text-center"><strong>Explore Projects</strong></h3>
  <div class="row m-4">
    <div
      class="col col-sm-4 mb-3"
      v-for="project in projects"
      :key="project.id"
    >
      <ProjectCard :project="project" />
    </div>
  </div>

  <h3 class="mt-3 text-center"><strong>Explore Users</strong></h3>
  <div class="row m-4">
    <div class="col col-sm-4 mb-3" v-for="user in users" :key="user.id">
      <UserCard :user="user" />
    </div>
  </div>
</template>

<script>
import ProjectCard from "@/components/ProjectCard.vue";
import UserCard from "@/components/UserCard.vue";

import { searchProjects } from "@/api/project";
import { searchUsers } from "@/api/user";

export default {
  name: "Explore",

  data() {
    return {
      query: "",
      projects: [],
      users: [],
    };
  },

  components: {
    ProjectCard,
    UserCard,
  },

  methods: {
    async search() {
      await this.fetchData();
      this.query = "";
    },

    async fetchData() {
      searchProjects(this.query)
        .then((response) => {
          this.projects = response.projects;
        })
        .catch((error) => {
          console.log(error);
        });

      searchUsers(this.query)
        .then((response) => {
          this.users = response.users;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  async created() {
    this.fetchData();
  },
};
</script>
