<template>
  <button
    type="button"
    class="btn"
    data-bs-toggle="modal"
    data-bs-target="#projectSettingsModal"
  >
    <font-awesome-icon icon="fa-solid fa-gear" />
  </button>

  <div
    class="modal fade"
    id="projectSettingsModal"
    tabindex="-1"
    aria-labelledby="projectSettingsModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <span> #id: {{ id }}</span>
          &emsp; &emsp;
          <h5 class="modal-title" id="projectSettingsModalLabel">
            {{ this.name }}
          </h5>

          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="form-check form-switch">
              <input
                class="form-check-input"
                type="checkbox"
                id="flexSwitchCheckChecked"
                v-model="new_is_public"
              />
              <label
                class="form-check-label"
                for="flexSwitchCheckChecked"
                style="padding-right: 3px"
              >
                Public
              </label>
              <button
                type="button"
                class="btn"
                style="padding: 0"
                data-toggle="tooltip"
                data-placement="right"
                title="Make this project visible to everyone. (Read Only)"
              >
                <font-awesome-icon
                  icon="fa-regular fa-circle-question"
                  class="p-1"
                />
              </button>
            </div>
            <div style="margin-top: 30px">
              <div>
                <span style="padding-right: 3px"> Shared </span>
                <button
                  type="button"
                  class="btn"
                  style="padding: 0"
                  data-toggle="tooltip"
                  data-placement="right"
                  title="The following users have write permissions on the project"
                >
                  <font-awesome-icon
                    icon="fa-regular fa-circle-question"
                    class="py-1"
                  />
                </button>
              </div>

              <div class="modal-body" style="padding: 0">
                <div class="card mb-3">
                  <div class="card-body">
                    <p
                      v-if="this.new_shared_users.length == 0"
                      class="card-text"
                    >
                      You have not shared this project with anyone.
                    </p>
                    <div v-else>
                      <router-link
                        v-for="username in this.new_shared_users"
                        @click="handleModalClick"
                        :key="username"
                        :to="`/profile/${username}`"
                        style="text-decoration: none; color: inherit"
                      >
                        <h5 class="card-title" style="font-size: large">
                          <img
                            :src="getAvatarUrl(username)"
                            class="rounded-circle"
                            alt="avatar"
                            style="width: 2rem; height: 2rem"
                          />
                          <strong class="m-2">@{{ username }} </strong>
                        </h5>
                      </router-link>
                    </div>
                  </div>
                </div>
              </div>
              <div style="margin-top: 30px">
                <ul class="nav justify-content-start">
                  <li class="nav-item">
                    <input
                      type="text"
                      class="form-control"
                      id="new-shared-user"
                      v-model="new_shared_user"
                      placeholder="New shared user"
                    />
                  </li>
                  <li class="nav-item mx-1">
                    <button
                      type="button"
                      class="btn btn-primary"
                      style="
                        background-color: var(--bs-purple);
                        border-color: var(--bs-purple);
                      "
                      @click="addSharedUser"
                    >
                      <font-awesome-icon icon="fa-solid fa-plus" />
                    </button>
                  </li>
                </ul>
              </div>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
            id="dismiss-modal"
          >
            Cancel
          </button>
          <button
            type="button"
            class="btn btn-success"
            data-dismiss="modal"
            @click="submitChanges"
            style="
              background-color: var(--bs-purple);
              border-color: var(--bs-purple);
            "
          >
            Save Changes
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MD5 from "crypto-js/md5";
import { changeProjectVisibility, shareProject } from "@/api/project.js";
function arrayEquals(a, b) {
  return (
    Array.isArray(a) &&
    Array.isArray(b) &&
    a.length === b.length &&
    a.every((val, index) => val === b[index])
  );
}
export default {
  name: "ProjectSettingsModal",
  props: {
    name: String,
    id: String,
    user: String, //TODO check if user is owner
    shared_users: Array,
    is_public: Boolean,
  },
  data() {
    return {
      new_shared_users: Array.from(this.shared_users),
      new_is_public: this.is_public,
    };
  },

  methods: {
    addSharedUser() {
      if (this.new_shared_user != "") {
        this.new_shared_users.push(this.new_shared_user);
        this.new_shared_user = "";
      }
    },
    propagateChanges() {
      this.$emit("update-project-visibility", {
        public: this.new_is_public,
        shared: this.new_shared_users,
      });
      document.getElementById("dismiss-modal").click();
    },
    handleModalClick() {
      document.getElementById("dismiss-modal").click();
    },

    getAvatarUrl(username) {
      let hash = MD5(username).toString();
      return `https://www.gravatar.com/avatar/${hash}?d=identicon`;
    },
    async updateSharedUsers() {
      let actual_shared_users = Array.from(this.shared_users);
      for (let user of this.new_shared_users) {
        if (!this.shared_users.includes(user)) {
          try {
            await shareProject(this.id, user);
            actual_shared_users.push(user);
          } catch (err) {
            alert("Error sharing project with " + user);
            continue;
          }
        }
      }
      this.new_shared_users = actual_shared_users;
    },
    async submitChanges() {
      if (this.new_is_public != this.is_public) {
        try {
          await changeProjectVisibility(this.id, this.new_is_public);
          console.log("changed visibility");
        } catch (err) {
          console.log(err);
          return;
        }
      }
      if (!arrayEquals(this.new_shared_users, this.shared_users)) {
        try {
          await this.updateSharedUsers();
          console.log("changed visibility");
        } catch (err) {
          console.log(err);
          return;
        }
      }
      this.propagateChanges();
    },
  },
};
</script>

<style scoped>
a {
  color: inherit;
  text-decoration: none;
}
</style>
