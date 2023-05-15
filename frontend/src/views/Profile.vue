<template>
  <div class="text-center mt-5" v-if="!username">
    <h2>
      <strong
        >Oops there's no user called "{{ this.$route.params.username }}"</strong
      >
    </h2>
    <h3>
      Maybe you were looking for <a href="https://youtu.be/dQw4w9WgXcQ">this</a>
    </h3>
  </div>

  <div class="text-center mt-3" v-if="username">
    <h2>
      <strong>@{{ username }}</strong>
      <EditProfileModal
        class="col"
        v-if="isCurrentUser"
        :firstName="firstName"
        :lastName="lastName"
        :email="email"
        @edit-profile="handleEditProfile"
      />
      <font-awesome-icon
        v-if="!isCurrentUser && !isFollowing"
        icon="fa-solid fa-user-plus"
        size="xs"
        class="ms-3"
        @click="toggleFollow"
        style="cursor: pointer; color: #005000"
      />
      <font-awesome-icon
        v-if="!isCurrentUser && isFollowing"
        icon="fa-solid fa-user-minus"
        size="xs"
        class="ms-3"
        @click="toggleFollow"
        style="cursor: pointer; color: #800000"
      />
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
      <ProjectCard :project="project" @favorite-changed="changeFavorite" />
    </div>
  </div>
</template>

<script>
import ProjectCard from "@/components/ProjectCard.vue";
import NewProjectModal from "@/components/NewProjectModal.vue";
import EditProfileModal from "@/components/EditProfileModal.vue";

import { getUser, followUser, editProfile } from "@/api/user.js";
import { createProject, getProject } from "@/api/project.js";

export default {
  name: "Profile",

  data() {
    return {
      username: "",
      email: "",
      firstName: "",
      lastName: "",
      dateJoined: new Date(),
      projects: [],
      isFollowing: false,
    };
  },

  async created() {
    getUser(this.$route.params.username)
      .then((response) => {
        this.username = response.user.username;
        this.email = response.user.email;
        this.firstName = response.user.first_name;
        this.lastName = response.user.last_name;
        this.dateJoined = new Date(response.user.date_joined);

        this.isFollowing = response.followers_usernames.includes(
          localStorage.getItem("username")
        );

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

    handleEditProfile(newProfile) {
      editProfile(newProfile.firstName, newProfile.lastName, newProfile.email)
        .then(() => {
          this.firstName = newProfile.firstName;
          this.lastName = newProfile.lastName;
          this.email = newProfile.email;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    changeFavorite(projectId) {
      let project = this.projects.find((project) => project.id == projectId);
      project.is_favorite = !project.is_favorite;
    },

    toggleFollow() {
      followUser(this.username, !this.isFollowing)
        .then(() => {
          this.isFollowing = !this.isFollowing;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  components: {
    ProjectCard,
    NewProjectModal,
    EditProfileModal,
  },

  computed: {
    isCurrentUser() {
      return this.username == localStorage.getItem("username");
    },

    fullName() {
      return this.firstName + " " + this.lastName;
    },
  },
};
</script>
