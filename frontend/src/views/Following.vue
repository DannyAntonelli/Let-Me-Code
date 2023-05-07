<template>
  <h3 class="mt-3 text-center">
    <strong>Projects of people you're following</strong>
  </h3>
  <div class="row m-4">
    <div
      class="col col-sm-4 mb-3"
      v-for="project in projects"
      :key="project.id"
    >
      <ProjectCard :project="project" @favorite-changed="changeFavorite" />
    </div>
  </div>
</template>

<script>
import { getUser } from "@/api/user";
import { getProject } from "@/api/project";

import ProjectCard from "@/components/ProjectCard.vue";

export default {
  name: "Following",

  data() {
    return {
      projects: [],
    };
  },

  async created() {
    getUser(this.username)
      .then((response) => response.following_usernames)
      .then((followingUsernames) => {
        for (let username of followingUsernames) {
          getUser(username)
            .then((response) => {
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
        }
      })
      .catch((error) => {
        console.log(error);
      });
  },

  computed: {
    username() {
      return localStorage.getItem("username");
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
  },

  components: {
    ProjectCard,
  },
};
</script>
