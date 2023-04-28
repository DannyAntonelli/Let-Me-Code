<template>
  <div id="code-editor" style="height: 500px"></div>
</template>

<script>
  import loader from "@monaco-editor/loader";

  export default {
    name: "CodeEditor",
    props: {
      file: String,
    },
    methods: {
      onChange: function (newValue, e) {
        console.log("onChange", newValue, e);
      },
    },
    async mounted() {
      const editorOptions = {
        language: "python",
        value: this.file.content,
        minimap: { enabled: false },

        options: {
          change: this.onChange,
          //   change: (e) => console.log(e),
        },
      };
      loader.init().then((monaco) => {
        let editor = monaco.editor;
        editor.create(document.getElementById("code-editor"), editorOptions);
        editor.onDidChangeModelContent = (e) => {
          console.log("onDidChangeModelContent", e);
        };
      });
    },
  };
</script>
