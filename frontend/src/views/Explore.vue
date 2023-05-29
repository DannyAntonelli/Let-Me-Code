<template>
  <div class="d-flex justify-content-center align-items-center mt-5 mb-2">
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

  <ul class="nav nav-tabs text-center justify-content-center">
    <li class="nav-item">
      <a :class="projectsNavLinkClass" @click="setProjectsPage" href="#"
        >Projects</a
      >
    </li>
    <li class="nav-item">
      <a :class="usersNavLinkClass" @click="setUsersTab" href="#">Users</a>
    </li>
  </ul>

  <div class="row m-4" v-if="projectsTab">
    <div
      class="col-12 col-sm-6 col-md-4 mb-3"
      v-for="project in projects"
      :key="project.id"
    >
      <ProjectCard :project="project" @favorite-changed="changeFavorite" />
    </div>
  </div>

  <div class="row m-4" v-if="!projectsTab">
    <div
      class="col-12 col-sm-6 col-md-4 mb-3"
      v-for="user in users"
      :key="user.id"
    >
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
      projectsTab: true,
    };
  },

  components: {
    ProjectCard,
    UserCard,
  },

  methods: {
    async search() {
      this.fetchData();
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

    setProjectsPage() {
      this.projectsTab = true;
    },

    setUsersTab() {
      this.projectsTab = false;
    },

    changeFavorite(projectId) {
      let project = this.projects.find((project) => project.id == projectId);
      project.is_favorite = !project.is_favorite;
    },
  },

  computed: {
    projectsNavLinkClass() {
      return "nav-link " + (this.projectsTab ? "active" : "");
    },

    usersNavLinkClass() {
      return "nav-link " + (this.projectsTab ? "" : "active");
    },
  },

  async created() {
    this.fetchData();
  },
};
</script>

<style scoped>
.input-group {
  width: 30rem;
}
</style>
