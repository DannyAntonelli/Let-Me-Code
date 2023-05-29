<template>
  <div class="text-center mt-5" v-if="projectNotFound">
    <h2>
      <strong
        >Oops there's no project with id "{{ this.$route.params.id }}"</strong
      >
    </h2>
    <h3>
      Maybe you were looking for
      <a class="rickroll-link" href="https://youtu.be/dQw4w9WgXcQ">this</a>
    </h3>
  </div>

  <div
    class="container-fluid text-center mt-2"
    style="padding-left: 20px; padding-right: 20px"
    v-if="this.id"
  >
    <div class="row">
      <div class="col-md-2">
        <div class="row text-start align-content-start">
          <TopBar
            :workspaceName="this.name"
            :workspaceId="this.id"
            :user="this.user"
            :shared_users="this.shared_users"
            :is_public="this.is_public"
            :editPermit="this.editPermit"
            v-on:update-project-visibility="updateProjectVisibility"
            :key="this.reloadFiles"
          />
        </div>
        <div class="row h-100" style="margin-left: 0; padding-left: 0">
          <div
            class="d-flex align-items-start flex-column h-100"
            style="margin-left: 0; padding-left: 0; width: 100%"
          >
            <div class="row" style="height: 90%">
              <SideBar
                :files="this.files"
                :proj_id="this.id"
                :currentFileId="this.currentFile ? this.currentFile.id : null"
                :key="this.reloadFiles"
                :editPermit="this.editPermit"
                v-on:refresh-files="refreshProject"
                v-on:file-clicked="changeFile"
              />
            </div>
            <div class="row h-10" style="margin-bottom: 40px">
              <BotBar
                :file="this.currentFile"
                :theme="this.editorTheme"
                :key="this.reloadFile"
                v-on:theme-changed="changeTheme"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-10">
        <CodeEditor
          :file="this.currentFile"
          :editorTheme="this.editorTheme"
          :key="this.reloadFile"
          :editPermit="this.editPermit"
          v-on:file-changed="updateFile"
          ref="editor"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { retrieveProjectInfo } from "@/components/workspace/utils.js";
import { getFile } from "@/api/file.js";
import CodeEditor from "@/components/workspace/CodeEditor.vue";
import TopBar from "@/components/workspace/TopBar.vue";
import BotBar from "@/components/workspace/BotBar.vue";
import SideBar from "@/components/workspace/SideBar.vue";

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
      files: [],
      currentFile: null,
      reloadFile: false,
      reloadFiles: false,
      editorTheme: "vs-dark",
      editPermit: false,
      projectNotFound: false,
    };
  },

  methods: {
    refreshProject() {
      retrieveProjectInfo(this.$route.params.id, this);
    },
    changeFile(file) {
      this.$refs.editor.storeChanges();
      this.currentFile = file;
      this.reloadFile = !this.reloadFile;
    },
    updateFile(file, content, saved) {
      file.content = content;
      file.saved = saved;
    },
    changeTheme(theme) {
      if (theme == this.editorTheme) return;
      this.editorTheme = theme;
      this.reloadFile = !this.reloadFile;
    },
    updateProjectVisibility(is_public, shared_users) {
      this.is_public = is_public;
      this.shared_users = shared_users;
    },
    setEditPermit() {
      console.log(this.user, "AJASHHASHA");
      this.editPermit =
        this.user == localStorage.getItem("username") ||
        this.shared_users.includes(localStorage.getItem("username"));
    },
    async getFiles() {
      this.files = [];
      for (let file_id of this.file_ids) {
        console.log(file_id);
        console.log("aaa    ");
        let f = await getFile(file_id);
        // .then((response) => {
        //   this.files.push(response); // Race condition?
        // })
        // .catch((error) => {
        //   console.log(error);
        // });
        f.file.saved = true;
        this.files.push(f.file);
      }
      this.reloadFiles = !this.reloadFiles;
    },
  },

  async beforeCreate() {
    retrieveProjectInfo(this.$route.params.id, this);
  },
};
</script>
