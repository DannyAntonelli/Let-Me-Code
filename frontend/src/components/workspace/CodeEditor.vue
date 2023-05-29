<template>
  <div id="no_file_open_warning" v-if="this.file === null">
    <div class="alert alert-warning" role="alert">No file open</div>
  </div>
  <div v-if="this.file != null">
    <div
      class="row justify-content-between"
      style="margin-left: 5px; margin-right: 10px"
    >
      <div class="col text-start py-2">
        <font-awesome-icon :icon="fileIcon" class="px-2" />
        <strong>{{ this.file.name }}</strong>
      </div>
      <div class="col text-end">
        <font-awesome-icon
          icon="fa-regular fa-floppy-disk"
          id="save-button"
          style="color: var(--workspace-blue); padding: 5px; cursor: pointer"
          v-if="this.status === 'edited'"
          @click="this.startSaving()"
        />
        <font-awesome-icon
          icon="fa-regular fa-floppy-disk"
          style="padding: 5px"
          v-if="this.status === 'saved' && this.editPermit === true"
        />
        <span
          style="color: var(--workspace-blue); padding: 5px"
          v-if="this.editPermit === false"
          >No Write Permission
        </span>
      </div>
    </div>

    <div class="text-start">
      <MonacoEditor
        class="editor"
        :options="this.options"
        style="height: 80vh !important; width: auto !important"
        @change="onChange"
        v-model="code"
        :key="this.file.id"
        @editorDidMount="editorDidMount"
        value=""
      />
    </div>
  </div>
</template>

<script>
import { h } from "vue";
import MonacoEditor from "vue-monaco";
import { syncFile } from "@/api/file.js";
MonacoEditor.render = () => h("div");
export default {
  name: "CodeEditor",
  props: {
    file: Object,
    editorTheme: String,
    editPermit: Boolean,
  },
  methods: {
    // eslint-disable-next-line no-unused-vars
    onChange: function (newValue, e) {
      if (newValue.isTrusted) return;
      this.content = newValue;
      this.status = "edited";
    },
    storeChanges: function () {
      if (this.status == "edited") {
        this.$emit("file-changed", this.file, this.content, false);
      }
    },
    editorDidMount(editor) {
      editor.onDidScrollChange((e) => {
        console.log(e, this.file);
      });
      window.addEventListener("keydown", this.onKeyPress);
    },
    onKeyPress(e) {
      console.log(e, this.file);
      if (e.ctrlKey) {
        e.preventDefault();
      }
      if (e.ctrlKey && e.key === "s") {
        console.log("saving", this.content);
        this.startSaving();
      }
    },
    startSaving() {
      this.status = "saving";
    },
  },
  watch: {
    status: function (newStatus) {
      if (newStatus === "saving") {
        if (this.editPermit === false) {
          this.status = "No Permission";
          return;
        }
        syncFile(this.file.id, this.content)
          .then((response) => {
            console.log(response);
            this.status = "saved";
            this.$emit("file-changed", this.file, this.content, true);
          })
          .catch((error) => {
            console.log(error);
            this.status = "error";
          });
      }
    },
  },
  data() {
    return {
      options: null,
      code: "const  noop = () => {}", // Not sure if this is needed
      status: "saved",
      content: "",
    };
  },

  computed: {
    fileIcon() {
      switch (this.file.language.toLowerCase()) {
        case "python":
          return "fa-brands fa-python";
        case "javascript":
          return "fa-brands fa-js-square";
        case "css":
          return "fa-brands fa-css3";
        case "html":
          return "fa-brands fa-html5";
        case "rust":
          return "fa-brands fa-rust";
        case "go":
          return "fa-brands fa-golang";
        case "php":
          return "fa-brands fa-php";
        case "java":
          return "fa-brands fa-java";
        default:
          return "fa-regular fa-file";
      }
    },
  },

  async mounted() {
    console.log("loading editor for", this.file);
    if (this.file === null) {
      return;
    }

    this.options = {
      language: this.file.language.toLowerCase(),
      value: this.file.content,
      theme: this.editorTheme,
      readOnly: !this.editPermit,
    };
    this.content = this.file.content;
    this.status = this.file.saved ? "saved" : "edited";
  },
  async unmounted() {
    window.removeEventListener("keydown", this.onKeyPress);
    console.log("unmounting editor", this.file);
  },
  components: {
    MonacoEditor,
  },
};
</script>
