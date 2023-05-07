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
                <li class="list-group-item">An item</li>
                <li
                  class="list-group-item"
                  v-for="user in this.new_shared_users"
                  :key="user"
                >
                  {{ user }}
                </li>
              </ul>
              <div class="mb-3" style="margin-top: 30px">
                <input
                  type="text"
                  class="form-control"
                  id="new-shared-user"
                  v-model="new_shared_user"
                />
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
  import { changeProjectVisibility } from "@/api/project.js";
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
        new_shared_users: this.shared_users,
        new_is_public: this.is_public,
      };
    },

    methods: {
      propagateChanges() {
        this.$emit("update-project-visibility", {
          public: this.new_is_public,
          shared: this.new_shared_users,
        });
        document.getElementById("dismiss-modal").click();
      },
      submitChanges() {
        if (this.new_is_public != this.is_public) {
          changeProjectVisibility(this.id, this.new_is_public)
            .then(() => {
              console.log("Project visibility changed");
              this.propagateChanges();
            })
            .catch((err) => {
              console.log(err);
            });
        } else if (this.new_shared_users != this.shared_users) {
          //TODO
        }
      },
    },
  };
</script>
