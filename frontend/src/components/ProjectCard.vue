<template>
  <div class="card hidden">
    <div class="card-body">
      <h5 class="card-title">
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
          class="star-favorite"
          @click="toggleFavorite"
        />
        <font-awesome-icon
          v-else
          icon="fa-regular fa-star"
          class="star-not-favorite"
          @click="toggleFavorite"
        />
        <font-awesome-icon
          icon="fa-solid fa-trash"
          class="trash-icon"
          @click="deleteProject"
          v-if="canDelete"
        />
      </h5>
      <router-link :to="profileUrl"
        ><h6 class="card-subtitle mb-2 text-muted">
          @{{ project.creator_username }}
        </h6></router-link
      >
      <p class="card-text">{{ project.description }}</p>
      <span
        v-for="language in project.languages"
        :key="language"
        class="badge rounded-pill text-bg-info m-1"
        >{{ language }}</span
      >
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
    canDelete: {
      type: Boolean,
      default: false,
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

    deleteProject() {
      this.$emit("delete-project", this.project.id);
    },
  },

  async mounted() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          observer.unobserve(entry.target);
          entry.target.classList.add("show");
        }
      });
    });

    document
      .querySelectorAll(".hidden")
      .forEach((element) => observer.observe(element));
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: inherit;
}

.card-title {
  font-size: large;
}

.star-favorite {
  color: gold;
  cursor: pointer;
}

.star-not-favorite {
  cursor: pointer;
}

.star-not-favorite:hover {
  color: gold;
}

.trash-icon {
  margin-left: 0.3rem;
  cursor: pointer;
}

.trash-icon:hover {
  color: var(--bs-danger);
}
</style>
