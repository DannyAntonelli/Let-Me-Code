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

    <h3 class="mt-5"><strong>Projects</strong></h3>
  </div>

  <div class="row m-4">
    <div
      class="col col-sm-4 mb-3"
      v-for="project in projects"
      :key="project.id"
    >
      <ProjectCard :project="project" />
    </div>
  </div>
</template>

<script>
import ProjectCard from "@/components/ProjectCard.vue";
import NewProjectModal from "@/components/NewProjectModal.vue";

import { getUser } from "@/api/user.js";
import { createProject, getProject } from "@/api/project.js";

export default {
  name: "Profile",

  data() {
    return {
      username: "",
      email: "",
      fullName: "",
      dateJoined: new Date(),
      projects: [],
    };
  },

  async created() {
    getUser(this.$route.params.username)
      .then((response) => {
        this.username = response.user.username;
        this.email = response.user.email;
        this.fullName =
          response.user.first_name + " " + response.user.last_name;
        this.dateJoined = new Date(response.user.date_joined);

        let projectIds = response.project_ids.concat(
          response.shared_project_ids
        );
        for (let projectId of projectIds) {
          getProject(projectId)
            .then((response) => {
              this.projects.push(response);
            })
            .catch((error) => {
              console.log(error);
            });
        }
      })
      .catch((error) => {
        console.log(error);
      });
  },

  methods: {
    handleCreateProject(newProject) {
      createProject(
        newProject.name,
        newProject.description,
        newProject.isPublic
      )
        .then((response) => {
          getProject(response.project_id)
            .then((response) => {
              this.projects.push(response);
            })
            .catch((error) => {
              console.log(error);
            });
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

  computed: {
    isCurrentUser() {
      return this.username == localStorage.getItem("username");
    },
  },
};
</script>
