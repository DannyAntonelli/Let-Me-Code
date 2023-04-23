<template>
  <div class="card">
    <div class="card-body">
      <router-link :to="projectUrl"
        ><h5 class="card-title">{{ title }}</h5></router-link
      >
      <router-link :to="profileUrl"
        ><h6 class="card-subtitle mb-2 text-muted">
          {{ creator }}
        </h6></router-link
      >
      <p class="card-text">{{ description }}</p>
    </div>
  </div>
</template>

<script>
import { getProject } from "@/api/project.js";

export default {
  name: "ProjectCard",
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },

  data() {
    return {
      title: "",
      description: "",
      isPublic: false,
      creator: "",
      sharedUsers: [],
      projectUrl: "",
      profileUrl: "",
    };
  },

  async created() {
    getProject(this.projectId)
      .then((response) => {
        this.title = response.project.name;
        this.description = response.project.description;
        this.isPublic = response.project.is_public;
        this.creator = response.creator_username;
        this.sharedUsers = response.shared_usernames;
        this.projectUrl = `/project/${this.projectId}`;
        this.profileUrl = `/profile/${this.creator}`;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: inherit;
}
</style>
