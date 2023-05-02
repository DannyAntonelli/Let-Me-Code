<template>
  <!-- <div>
        <h1>Workspace</h1>
        <p>{{ $route.params.id }}</p>
        <p>{{ name }}</p>
        <p>{{ description }}</p>
        <p>{{ is_public }}</p>
        <p>{{ user }}</p>
        <p>{{ shared_users }}</p>
        <p>{{ file_ids }}</p>
    </div> -->
  <div class="container text-center">
    <div class="row text-start">
      <TopBar :workspaceName="this.name" :workspaceId="this.id" />
    </div>
    <div class="row align-items-start">
      <div class="col-2">
        <SideBar
          :file_ids="this.file_ids"
          :proj_id="this.id"
          :currentFileId="this.currentFile ? this.currentFile.id : null"
          :key="this.file_ids"
          v-on:refresh-files="refreshProject"
          v-on:file-clicked="changeFile"
        />
      </div>
      <div class="col-10">
        <CodeEditor :file="this.currentFile" :key="this.currentFile" />
      </div>
    </div>
    <div class="row">
      <BotBar :file="this.currentFile" :key="this.currentFile" />
    </div>
  </div>
</template>

<script>
  import { getProject } from "@/api/project.js";
  import CodeEditor from "@/components/workspace/CodeEditor.vue";
  import TopBar from "@/components/workspace/TopBar.vue";
  import BotBar from "@/components/workspace/BotBar.vue";
  import SideBar from "@/components/workspace/SideBar.vue";
  function retrieveProjectInfo(id, context) {
    getProject(id)
      .then((response) => {
        console.log(response);
        context.file_ids = response.file_ids;
        context.description = response.description;
        context.id = response.id;
        context.is_public = response.is_public;
        context.name = response.name;
        context.shared_users = response.shared_users;
        context.user = response.user;
      })
      .catch((error) => {
        console.log(error);
      });
  }
  export default {
    name: "Workspace",

    components: {
      CodeEditor,
      TopBar,
      BotBar,
      SideBar,
    },
    data() {
      return {
        file_ids: [],
        description: "",
        id: "",
        is_public: false,
        name: "",
        shared_users: [],
        user: "",
        // currentFile: {
        //   id: 1,
        //   name: "/file1",
        //   content: "CIAOOOO",
        //   language: "python",
        //   project: 1,
        // },
        currentFile: null,
        // componentKey: 0,
      };
    },
    methods: {
      refreshProject() {
        retrieveProjectInfo(this.$route.params.id, this);
      },
      changeFile(file) {
        this.currentFile = file;
      },
    },
    async beforeCreate() {
      retrieveProjectInfo(this.$route.params.id, this);
    },
  };
</script>
