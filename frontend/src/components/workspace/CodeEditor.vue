<template>
  <div class="container text-start">
    <MonacoEditor
      class="editor"
      :options="this.options"
      style="height: 500px"
      @change="onChange"
      v-model="code"
      :key="this.file.id"
    />
  </div>
</template>

<script>
  import { h } from "vue";
  import MonacoEditor from "vue-monaco";
  MonacoEditor.render = () => h("div");
  export default {
    name: "CodeEditor",
    props: {
      file: Object,
    },
    methods: {
      onChange: function (newValue, e) {
        console.log("onChange", newValue, e, this.code);
      },
    },
    data() {
      return {
        options: {
          language: "python",
          value: this.file.content,
          theme: "vs-dark",
        },
        code: "const  noop = () => {}", // Not sure if this is needed
      };
    },
    components: {
      MonacoEditor,
    },
  };
</script>
