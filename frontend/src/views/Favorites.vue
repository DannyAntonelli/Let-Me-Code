<template>
  <h3 class="mt-5 mb-1 text-center"><strong>Favorite Projects</strong></h3>
  <div class="row m-4">
    <div
      class="col-12 col-sm-6 col-md-4 mb-3"
      v-for="project in favorites"
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
  name: "Favorites",

  data() {
    return {
      favorites: [],
    };
  },

  async created() {
    getUser(this.username)
      .then((response) => {
        let projectIds = response.favorite_project_ids;

        for (let projectId of projectIds) {
          getProject(projectId)
            .then((response) => {
              this.favorites.push(response);
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
      let project = this.favorites.find((project) => project.id == projectId);
      project.is_favorite = !project.is_favorite;
      this.favorites = this.favorites.filter(
        (project) => project.id != projectId
      );
    },
  },

  components: {
    ProjectCard,
  },
};
</script>
