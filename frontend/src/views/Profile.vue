<template>
  <div class="text-center mt-5" v-if="!username">
    <h2>
      <strong
        >Oops there's no user called "{{ this.$route.params.username }}"</strong
      >
    </h2>
    <h3>
      Maybe you were looking for
      <a class="rickroll-link" href="https://youtu.be/dQw4w9WgXcQ">this</a>
    </h3>
  </div>

  <div class="text-center mt-3" v-if="username">
    <img
      :src="getAvatarUrl(username)"
      class="rounded-circle mb-3"
      alt="avatar"
      style="height: 7rem"
    />

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
        style="cursor: pointer; color: var(--bs-success)"
      />

      <font-awesome-icon
        v-if="!isCurrentUser && isFollowing"
        icon="fa-solid fa-user-minus"
        size="xs"
        class="ms-3"
        @click="toggleFollow"
        style="cursor: pointer; color: var(--bs-danger)"
      />
    </h2>

    <h6>
      <a
        class="badge text-badge bg-primary mx-2"
        href="#"
        data-bs-toggle="modal"
        data-bs-target="#followersModal"
        style="cursor: pointer; text-decoration: none"
        >{{ followersUsernames.length }} followers</a
      >
      <a
        class="badge text-badge bg-primary"
        href="#"
        data-bs-toggle="modal"
        data-bs-target="#followingModal"
        style="cursor: pointer; text-decoration: none"
      >
        {{ followingUsernames.length }} following</a
      >
    </h6>

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
      class="col-12 col-sm-6 col-md-4 mb-3"
      v-for="project in projects"
      :key="project.id"
    >
      <ProjectCard
        :project="project"
        :canDelete="isDeleteAllowed(project)"
        @favorite-changed="changeFavorite"
        @delete-project="deleteProject"
      />
    </div>
  </div>

  <div
    class="modal fade"
    id="followersModal"
    tabindex="-1"
    aria-labelledby="followersModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="followersModalLabel">
            {{ this.followersUsernames.length }} Followers
          </h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
            id="dismiss-followers-modal"
          ></button>
        </div>
        <div class="modal-body">
          <div class="card mb-3">
            <div class="card-body">
              <p v-if="followersUsernames.length == 0" class="card-text">
                No followers yet
              </p>
              <div v-else>
                <router-link
                  v-for="followerUsername in followersUsernames"
                  @click="handleFollowersModalClick"
                  :key="followerUsername"
                  :to="`/profile/${followerUsername}`"
                  style="text-decoration: none"
                >
                  <h5 class="card-title" style="font-size: large">
                    <img
                      :src="getAvatarUrl(username)"
                      class="rounded-circle"
                      alt="avatar"
                      style="width: 2rem; height: 2rem"
                    />
                    <strong class="m-2">@{{ followerUsername }} </strong>
                  </h5>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div
    class="modal fade"
    id="followingModal"
    tabindex="-1"
    aria-labelledby="followingModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="followingModalLabel">
            {{ this.followingUsernames.length }} Following
          </h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
            id="dismiss-following-modal"
          ></button>
        </div>
        <div class="modal-body">
          <div class="card mb-1">
            <div class="card-body">
              <p v-if="followingUsernames.length == 0" class="card-text">
                No following yet
              </p>
              <div v-else>
                <router-link
                  v-for="followingUsername in followingUsernames"
                  :to="`/profile/${followingUsername}`"
                  :key="followingUsername"
                  @click="handleFollowingModalClick"
                  style="text-decoration: none"
                >
                  <h5 class="card-title" style="font-size: large">
                    <img
                      :src="getAvatarUrl(followingUsername)"
                      class="rounded-circle"
                      alt="avatar"
                      style="width: 2rem; height: 2rem"
                    />
                    <strong class="m-2">@{{ followingUsername }} </strong>
                  </h5>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MD5 from "crypto-js/md5";

import ProjectCard from "@/components/ProjectCard.vue";
import NewProjectModal from "@/components/NewProjectModal.vue";
import EditProfileModal from "@/components/EditProfileModal.vue";

import { getUser, followUser, editProfile } from "@/api/user.js";
import { createProject, getProject, deleteProject } from "@/api/project.js";

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
      followersUsernames: [],
      followingUsernames: [],
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
        this.followersUsernames = response.followers_usernames;
        this.followingUsernames = response.following_usernames;

        this.isFollowing = this.followersUsernames.includes(
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
          if (this.isFollowing) {
            this.followersUsernames.push(localStorage.getItem("username"));
          } else {
            this.followersUsernames = this.followersUsernames.filter(
              (username) => username != localStorage.getItem("username")
            );
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    handleFollowersModalClick() {
      document.getElementById("dismiss-followers-modal").click();
    },

    handleFollowingModalClick() {
      document.getElementById("dismiss-following-modal").click();
    },

    getAvatarUrl(username) {
      let hash = MD5(username).toString();
      return `https://www.gravatar.com/avatar/${hash}?d=identicon`;
    },

    isDeleteAllowed(project) {
      return (
        this.username == localStorage.getItem("username") &&
        project.creator_username == this.username
      );
    },

    deleteProject(projectId) {
      console.log(projectId);
      deleteProject(projectId)
        .then(() => {
          this.projects = this.projects.filter(
            (project) => project.id != projectId
          );
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

<style scoped>
a {
  color: inherit;
}
</style>
