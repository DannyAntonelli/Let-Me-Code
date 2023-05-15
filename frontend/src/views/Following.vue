<template>
  <h3 class="mt-3 text-center">
    <strong>People you're following</strong>
  </h3>

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
      class="col col-sm-4 mb-3"
      v-for="project in projects"
      :key="project.id"
    >
      <ProjectCard :project="project" @favorite-changed="changeFavorite" />
    </div>
  </div>

  <div class="row m-4" v-if="!projectsTab">
    <div class="col col-sm-4 mb-3" v-for="user in users" :key="user.id">
      <UserCard :user="user" />
    </div>
  </div>
</template>

<script>
import { getFollowingUsers } from "@/api/user";
import { getFollowingProjects } from "@/api/project";

import ProjectCard from "@/components/ProjectCard.vue";
import UserCard from "@/components/UserCard.vue";

export default {
  name: "Following",

  data() {
    return {
      projects: [],
      users: [],
      projectsTab: true,
    };
  },

  async created() {
    getFollowingProjects(this.query)
      .then((response) => {
        this.projects = response.projects;
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      });

    getFollowingUsers(this.query)
      .then((response) => {
        this.users = response.users;
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      });
  },

  computed: {
    username() {
      return localStorage.getItem("username");
    },

    projectsNavLinkClass() {
      return "nav-link " + (this.projectsTab ? "active" : "");
    },

    usersNavLinkClass() {
      return "nav-link " + (this.projectsTab ? "" : "active");
    },
  },

  methods: {
    changeFavorite(projectId) {
      let project = this.projects.find((project) => project.id == projectId);
      project.is_favorite = !project.is_favorite;
      this.projects = this.projects.filter(
        (project) => project.id != projectId
      );
    },

    setProjectsPage() {
      this.projectsTab = true;
    },

    setUsersTab() {
      this.projectsTab = false;
    },
  },

  components: {
    ProjectCard,
    UserCard,
  },
};
</script>
