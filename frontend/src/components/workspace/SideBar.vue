<template>
  Side

  <!-- <div v-for="file_id in files" :key="file_id">
    {{ file_id }}
  </div> -->
  <DirTree
    :node="this.tree"
    :key="this.tree"
    :root="this"
    :onFileClick="onFileClick"
  />
  <ContextMenu
    :items="menuItems"
    :position="menuPosition"
    :visible="menuVisible"
    :param="menuParam"
    v-on:close-context="resetContextMenu"
  />
  <NewFileModal
    :path="this.newFilePath"
    :key="newFilePath"
    v-on:close-modal="resetNewFilePath"
    v-on:submit-file="handleCreateFile"
  />
</template>

<script>
  // declare interface File {
  //     cod: string,
  //     param: string
  // }
  // eslint-disable-next-line no-unused-vars
  import { deleteFile } from "@/api/file.js";
  import DirTree from "@/components/workspace/DirTree.vue";
  import ContextMenu from "@/components/workspace/ContextualMenu.vue";
  import NewFileModal from "@/components/workspace/NewFileModal.vue";
  import { createFile } from "@/api/project.js";

  function buildTree(files) {
    let tree = {};
    for (let file of files) {
      let path = file.name.split("/");
      let curr = tree;
      for (let i = 0; i < path.length; i++) {
        if (i == path.length - 1) {
          file.fileName = path[i];
          curr[path[i]] = file;
        } else {
          if (curr[path[i]] == undefined) {
            curr[path[i]] = {
              folderName: path.slice(0, i + 1).join("/") + "/",
            };
          }
          curr = curr[path[i]];
        }
      }
    }
    tree["root"] = tree[""];
    delete tree[""];
    if (tree["root"] == undefined) {
      tree["root"] = {
        folderName: "/",
      };
    }
    console.log(tree);
    return tree;
  }
  export default {
    name: "SideBar",
    props: {
      files: Array,
      proj_id: String,
    },
    components: {
      DirTree,
      ContextMenu,
      NewFileModal,
    },
    data() {
      return {
        tree: {},
        //context menu
        menuFolderItems: [
          {
            label: "New File",
            action: (folder) => {
              //   this.showing = true;
              console.log("New File in", folder);
              this.newFilePath = folder;
              console.log(this.newFilePath);
            },
          },
          {
            label: "Delete",

            action: (a) => {
              console.log("Folder Delete", a);
              alert("Folder Delete Not Implemented Yet");
            },
          },
        ],
        menuFileItems: [
          {
            label: "Delete",
            action: (a) => {
              console.log("File deleted", a);
              deleteFile(a.id)
                .then((response) => {
                  console.log(response);
                  this.$emit("refresh-files");
                })
                .catch((error) => {
                  console.log(error);
                });
            },
          },
        ],
        menuItems: this.menuFolderItems,
        menuPosition: { x: 0, y: 0 },
        menuVisible: false,
        menuParam: null,
        //Modal
        showingNewFileModal: false,
        newFilePath: null,
      };
    },
    methods: {
      showMenu(event, file, name) {
        event.preventDefault();
        if (!file) {
          this.menuItems = this.menuFolderItems;
          console.log("folder");
        } else {
          this.menuItems = this.menuFileItems;
        }
        this.menuPosition.x = event.clientX;
        this.menuPosition.y = event.clientY;
        this.menuVisible = true;
        this.menuParam = name;
      },
      resetNewFilePath() {
        console.log("reset");
        this.newFilePath = null;
      },
      resetContextMenu() {
        console.log("reset context");
        this.menuVisible = false;
      },
      onFileClick(file) {
        console.log("file clicked", file);
        this.$emit("file-clicked", file);
      },
      handleCreateFile(newFile) {
        console.log("create file", newFile, this.proj_id);
        createFile(this.proj_id, newFile.name, newFile.language)
          .then((response) => {
            console.log(response);
            this.$emit("refresh-files");
          })
          .catch((error) => {
            console.log(error);
          });
      },
    },
    async created() {
      //   this.files = [
      //     { id: 1, name: "/file1", content: "", language: "py", project: 1 },
      //     { id: 2, name: "/file3", content: "", language: "py", project: 1 },
      //     {
      //       id: 3,
      //       name: "/folder/file2",
      //       content: "",
      //       language: "py",
      //       project: 1,
      //     },
      //     {
      //       id: 4,
      //       name: "/folder/file5",
      //       content: "",
      //       language: "py",
      //       project: 1,
      //     },
      //   ];
      console.log(this.files);
      let tree = buildTree(this.files);
      console.log(tree);
      this.tree = tree;
    },
  };
</script>
