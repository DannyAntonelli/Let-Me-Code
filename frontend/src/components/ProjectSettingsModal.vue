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
              <label class="form-check-label" for="flexSwitchCheckChecked"
                >Public</label
              >
            </div>
            <div v-if="!new_is_public">
              <ul class="list-group">
                <li class="list-group-item">Shared With:</li>
                <li
                  class="list-group-item"
                  v-for="user in this.new_shared_users"
                  :key="user"
                >
                  {{ user }}
                </li>
              </ul>
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
                  <li class="nav-item">
                    <button
                      type="button"
                      class="btn btn-primary"
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
          >
            Save Changes
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
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
      async updateSharedUsers() {
        for (let user of this.new_shared_users) {
          if (!this.shared_users.includes(user)) {
            await shareProject(this.id, user);
          }
        }
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
        if (
          !this.new_is_public &&
          !arrayEquals(this.new_shared_users, this.shared_users)
        ) {
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
