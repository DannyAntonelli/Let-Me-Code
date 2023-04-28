<template>
  <div class="card">
    <div class="card-body">
      <router-link :to="projectUrl"
        ><h5 class="card-title" style="font-size: large">
          <font-awesome-icon icon="fa-solid fa-code" size="xs" />
          <strong class="m-2">
            {{ project.name }}
          </strong>
          <span v-if="project.is_public" class="badge text-bg-success"
            >Public</span
          >
          <span v-if="!project.is_public" class="badge text-bg-secondary"
            >Private</span
          >
        </h5></router-link
      >
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
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: inherit;
}
</style>
