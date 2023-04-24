<template>
  <h1>{{ username }}</h1>

  <NewProjectModal @submit-project="handleCreateProject" v-if="isCurrentUser" />

  <p>email: {{ email }}</p>
  <p>first name: {{ firstName }}</p>
  <p>last name: {{ lastName }}</p>
  <p>date joined: {{ dateJoined }}</p>
  <p>Projects:</p>

  <div class="row">
    <div class="col-4" v-for="projectId in projectIds" :key="projectId">
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
      firstName: "",
      lastName: "",
      dateJoined: "",
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
    NewProjectModal,
  },
};
</script>
