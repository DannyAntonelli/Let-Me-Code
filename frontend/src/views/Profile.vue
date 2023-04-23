<template>
  <h1>{{ username }}</h1>
  <p>email: {{ email }}</p>
  <p>first name: {{ firstName }}</p>
  <p>last name: {{ lastName }}</p>
  <p>date joined: {{ dateJoined }}</p>
  <p>Projects:</p>

  <div class="row">
    <div
      class="col-sm-6 col-md-4 col-lg-3"
      v-for="projectId in projectIds"
      :key="projectId"
    >
      <ProjectCard :projectId="projectId" />
    </div>
  </div>

  <form @submit.prevent="handleCreateProject">
    <div class="form-outline mb-4">
      <input
        type="text"
        id="create-project-name"
        class="form-control"
        v-model="newProjectName"
        required
      />
      <label class="form-label" for="create-project-name">Project Name</label>
    </div>

    <div class="form-outline mb-4">
      <input
        type="text"
        id="create-project-description"
        class="form-control"
        v-model="newProjectDescription"
        required
      />
      <label class="form-label" for="create-project-description"
        >Project Description</label
      >
    </div>

    <div class="form-outline mb-4">
      <input
        type="checkbox"
        id="create-project-is-public"
        class="form-check-input"
        v-model="newProjectIsPublic"
      />
      <label class="form-check-label" for="create-project-is-public"
        >Public</label
      >
    </div>

    <button type="submit" class="btn btn-primary btn-block mb-4">
      Create Project
    </button>
  </form>
</template>

<script>
import ProjectCard from "@/components/ProjectCard.vue";

import { getUser } from "@/api/user.js";
import { createProject } from "@/api/project.js";

export default {
  name: "Profile",

  data() {
    return {
      username: "",
      email: "",
      firstName: "",
      lastName: "",
      dateJoined: "",
      projectIds: [],
      isCurrentUser: false,
      newProjectName: "",
      newProjectDescription: "",
      newProjectIsPublic: false,
    };
  },

  async created() {
    this.retrieveUserInfo();
  },

  methods: {
    handleCreateProject() {
      createProject(
        this.newProjectName,
        this.newProjectDescription,
        this.newProjectIsPublic
      )
        .then((response) => {
          console.log(response);
          this.retrieveUserInfo();
        })
        .catch((error) => {
          console.log(error);
        });
    },

    async retrieveUserInfo() {
      getUser(this.$route.params.username)
        .then((response) => {
          console.log(response);
          this.username = response.user.username;
          this.email = response.user.email;
          this.firstName = response.user.first_name;
          this.lastName = response.user.last_name;
          this.dateJoined = response.user.date_joined;
          this.projectIds = response.project_ids.concat(
            response.shared_project_ids
          );
          this.isCurrentUser =
            this.username == localStorage.getItem("username");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  components: {
    ProjectCard,
  },
};
</script>
