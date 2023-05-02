<template>
  <!-- <button
    type="button"
    class="btn btn-success"
    data-bs-toggle="modal"
    data-bs-target="#newFileModal"
  >
    New File
  </button> -->

  <div
    class="modal fade"
    id="newFileModal"
    tabindex="-1"
    aria-labelledby="newFileModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="newFileModalLabel">New File</h5>
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
                id="new-file-name"
                v-model="newName"
              />
            </div>

            <div class="mb-3">
              <input
                type="text"
                class="form-control"
                id="new-file-language"
                placeholder="Language"
                v-model="language"
              />
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
            @click="submitFile"
          >
            Create file
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { Modal } from "bootstrap";
  export default {
    name: "NewFileModal",

    data() {
      return {
        language: "",
        newName: "",
      };
    },
    props: {
      path: String,
    },
    methods: {
      submitFile() {
        this.$emit("submit-file", {
          name: this.newName,
          language: this.language,
        });
        document.getElementById("dismiss-modal").click();
        console.log(this.path, this.language);
      },
    },
    async mounted() {
      console.log(this.path, "aaaaaaaaa");
      this.newName = this.path;
      let m = new Modal(document.querySelector("#newFileModal"));
      if (this.path != null) {
        m.show();
      }
      var myModalEl = document.getElementById("newFileModal");
      myModalEl.addEventListener("hidden.bs.modal", (e) => {
        console.log("hidden", e);
        this.$emit("close-modal");
      });
    },
  };
</script>
