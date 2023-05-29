<template>
  <button
    type="button"
    class="btn btn-success"
    data-bs-toggle="modal"
    data-bs-target="#newProjectModal"
  >
    New Project
  </button>

  <div
    class="modal fade"
    id="newProjectModal"
    tabindex="-1"
    aria-labelledby="newProjectModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="newProjectModalLabel">New Project</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <input
                type="text"
                class="form-control"
                id="new-project-name"
                placeholder="Name"
                v-model="name"
              />
            </div>

            <div class="mb-3">
              <textarea
                class="form-control"
                id="new-project-description"
                placeholder="Description"
                v-model="description"
              ></textarea>
            </div>

            <div class="form-check form-switch">
              <input
                class="form-check-input"
                type="checkbox"
                id="flexSwitchCheckChecked"
                v-model="isPublic"
                checked
              />
              <label class="form-check-label" for="flexSwitchCheckChecked">
                Public
              </label>
              <button
                type="button"
                class="btn"
                id="public-project-tooltip"
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
          </form>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
            id="dismiss-new-project-modal"
          >
            Cancel
          </button>
          <button
            type="button"
            class="btn btn-success"
            data-dismiss="modal"
            @click="submitProject"
            style="
              background-color: var(--bs-purple);
              border-color: var(--bs-purple);
            "
          >
            Create project
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NewProjectModal",

  data() {
    return {
      name: "",
      description: "",
      isPublic: true,
    };
  },

  methods: {
    submitProject() {
      this.$emit("submit-project", {
        name: this.name,
        description: this.description,
        isPublic: this.isPublic,
      });
      document.getElementById("dismiss-new-project-modal").click();
      this.name = "";
      this.description = "";
      this.isPublic = true;
    },
  },
};
</script>

<style scoped>
#new-project-description {
  height: 20vh;
}

#public-project-tooltip {
  padding: 0;
}

.form-switch {
  text-align: left;
}

.form-check-label {
  padding-right: 3px;
}
</style>
