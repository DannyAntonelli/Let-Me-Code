<template>
  <h1>{{ username }}</h1>
  <p>email: {{ email }}</p>
  <p>first name: {{ firstName }}</p>
  <p>last name: {{ lastName }}</p>
  <p>date joined: {{ dateJoined }}</p>
  <ul>
    project ids:
    <li v-for="projectId in projectIds" :key="projectId">
      {{ projectId }}
    </li>
  </ul>
  <ul>
    shared project ids:
    <li v-for="sharedProjectId in sharedProjectIds" :key="sharedProjectId">
      {{ sharedProjectId }}
    </li>
  </ul>

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
      sharedProjectIds: [],
      isCurrentUser: false,
      newProjectName: "",
      newProjectDescription: "",
      newProjectIsPublic: false,
    };
  },

  async created() {
    getUser(this.$route.params.username)
      .then((response) => {
        console.log(response);
        this.username = response.user.username;
        this.email = response.user.email;
        this.firstName = response.user.first_name;
        this.lastName = response.user.last_name;
        this.dateJoined = response.user.date_joined;
        this.projectIds = response.project_ids;
        this.sharedProjectIds = response.shared_project_ids;
        this.isCurrentUser = this.username == localStorage.getItem("username");
      })
      .catch((error) => {
        console.log(error);
      });
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
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
