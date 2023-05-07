<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title" style="font-size: large">
        <router-link :to="projectUrl" class="m-1">
          <font-awesome-icon icon="fa-solid fa-code" size="xs" />
          <strong class="m-2">
            {{ project.name }}
          </strong>
          <span v-if="project.is_public" class="badge text-bg-success"
            >Public</span
          >
          <span v-else class="badge text-bg-secondary">Private</span>
        </router-link>
        <font-awesome-icon
          v-if="project.is_favorite"
          icon="fa-solid fa-star"
          @click="toggleFavorite"
        />
        <font-awesome-icon
          v-else
          icon="fa-regular fa-star"
          @click="toggleFavorite"
        />
      </h5>
      <router-link :to="profileUrl"
        ><h6 class="card-subtitle mb-2 text-muted">
          @{{ project.creator_username }}
        </h6></router-link
      >
      <p class="card-text">{{ project.description }}</p>
    </div>
  </div>
</template>

<script>
import { changeFavorite } from "@/api/project";

export default {
  name: "ProjectCard",

  props: {
    project: {
      type: Object,
      required: true,
    },
  },

  computed: {
    projectUrl() {
      return `/project/${this.project.id}`;
    },

    profileUrl() {
      return `/profile/${this.project.creator_username}`;
    },
  },

  methods: {
    toggleFavorite() {
      changeFavorite(this.project.id, !this.project.is_favorite)
        .then(() => {
          this.$emit("favorite-changed", this.project.id);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: inherit;
}
</style>
