<template>
  <div id="no_file_open_warning" v-if="this.file === null">
    <div class="alert alert-warning" role="alert">No file open</div>
  </div>
  <div v-if="this.file != null">
    {{ this.status }}
    <div class="container text-start">
      <MonacoEditor
        class="editor"
        :options="this.options"
        style="height: 500px"
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
    },
    methods: {
      onChange: function (newValue, e) {
        console.log("onChange", newValue, e, this.code);
        this.content = newValue;
      },
      editorDidMount(editor) {
        // TODO On editor unmount
        editor.onDidScrollChange((e) => {
          console.log(e);
        });
        window.addEventListener("keydown", (e) => {
          console.log(e);
          if (e.ctrlKey) {
            e.preventDefault();
          }
          if (e.ctrlKey && e.key === "s") {
            console.log("saving", this.content);
            this.status = "saving";
          }
        });
      },
    },
    watch: {
      status: function (newStatus) {
        if (newStatus === "saving") {
          syncFile(this.file.id, this.content)
            .then((response) => {
              console.log(response);
              this.status = "saved";
              this.$emit("file-changed", this.file, this.content);
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
        language: "python",
        value: this.file.content,
        theme: "vs-dark",
      };
      this.content = this.file.content;
    },
    components: {
      MonacoEditor,
    },
  };
</script>
