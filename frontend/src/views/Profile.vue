<template>
  <div class="text-center mt-3">
    <h2>
      <strong>@{{ username }}</strong>
    </h2>
    <p class="text-muted mb-0" v-if="fullName.length > 1">{{ fullName }}</p>
    <p class="text-muted mb-0" v-if="email">{{ email }}</p>
    <p class="text-muted">Member since: {{ dateJoined.toDateString() }}</p>
    <NewProjectModal
      @submit-project="handleCreateProject"
      v-if="isCurrentUser"
    />

    <h3 class="mt-5"><strong>Projects:</strong></h3>
  </div>

  <div class="row m-4">
    <div
      class="col col-sm-4 mb-3"
      v-for="projectId in projectIds"
      :key="projectId"
    >
      <ProjectCard :projectId="projectId" />
    </div>
  </div>
</template>

<script>
import ProjectCard from "@/components/ProjectCard.vue";
import NewProjectModal from "@/components/NewProjectModal.vue";

import { getUser } from "@/api/user.js";
import { createProject } from "@/api/project.js";

export default {
  name: "Profile",

  data() {
    return {
      username: "",
      email: "",
      fullName: "",
      dateJoined: new Date(),
      projectIds: [],
      isCurrentUser: false,
    };
  },

  async created() {
    this.retrieveUserInfo();
  },

  methods: {
    handleCreateProject(newProject) {
      createProject(
        newProject.name,
        newProject.description,
        newProject.isPublic
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
          this.fullName =
            response.user.first_name + " " + response.user.last_name;
          this.dateJoined = new Date(response.user.date_joined);
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
    NewProjectModal,
  },
};
</script>
