<template>
  <div id="no_file_open_warning" v-if="this.file === null">
    <div class="alert alert-warning" role="alert">No file open</div>
  </div>
  <div v-if="this.file != null">
    <div
      class="row justify-content-between"
      style="margin-left: 10px; margin-right: 10px"
    >
      <div class="col text-start">{{ this.file.name }}</div>
      <div class="col text-end">
        {{ this.status }}
        <font-awesome-icon
          icon="fa-regular fa-floppy-disk"
          style="color: #ce1c1c"
          v-if="this.status === 'edited'"
          @click="this.startSaving()"
        />
        <font-awesome-icon
          icon="fa-regular fa-floppy-disk"
          style="color: #1cce1c"
          v-if="this.status === 'saved'"
        />
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
            alert("You do not have permission to edit this file");
            this.status = "Error Saving No Permission";
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

    async mounted() {
      console.log("loading editor for", this.file);
      if (this.file === null) {
        return;
      }

      this.options = {
        language: this.file.language.toLowerCase(),
        value: this.file.content,
        theme: this.editorTheme,
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
