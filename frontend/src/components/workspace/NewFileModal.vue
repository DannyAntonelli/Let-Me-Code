<template>
  <div
    class="modal fade"
    id="newFileModal"
    tabindex="-1"
    aria-labelledby="newFileModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="newFileModalLabel">New File</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            id="close-modal"
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

            <div class="mb-3 text-start">
              <div class="dropdown">
                <button
                  class="btn btn-secondary dropdown-toggle"
                  type="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  {{ language }}
                </button>
                <ul class="dropdown-menu">
                  <li v-for="lang in this.languages" :key="lang">
                    <a class="dropdown-item" @click="selectLang(lang)">{{
                      lang
                    }}</a>
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
import { languages } from "@/variables.js";
export default {
  name: "NewFileModal",
  data() {
    return {
      languages: languages,
      language: "python",
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
      document.getElementById("close-modal").click();
      console.log(this.path, this.language);
    },
    selectLang(lang) {
      this.language = lang;
    },
  },
  async mounted() {
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
