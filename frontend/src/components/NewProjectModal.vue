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
                style="height: 20vh"
                v-model="description"
              ></textarea>
            </div>

            <div class="form-check form-switch">
              <input
                class="form-check-input"
                type="checkbox"
                id="flexSwitchCheckChecked"
                v-model="isPublic"
              />
              <label class="form-check-label" for="flexSwitchCheckChecked"
                >Public</label
              >
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
            @click="submitProject"
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
      document.getElementById("dismiss-modal").click();
      this.name = "";
      this.description = "";
      this.isPublic = true;
    },
  },
};
</script>
