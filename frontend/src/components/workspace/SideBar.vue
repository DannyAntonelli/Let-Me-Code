<template>
  <DirTree
    :node="this.tree"
    :key="this.tree"
    :root="this"
    :onFileClick="onFileClick"
    :currentFileId="this.currentFileId"
  />
  <ContextMenu
    :items="menuItems"
    :position="menuPosition"
    :visible="menuVisible"
    :param="menuParam"
    v-on:close-context="resetContextMenu"
    v-if="this.editPermit"
  />
  <NewFileModal
    :path="this.newFilePath"
    :key="newFilePath"
    v-on:close-modal="resetNewFilePath"
    v-on:submit-file="handleCreateFile"
  />
</template>

<script>
  import { deleteFile } from "@/api/file.js";
  import DirTree from "@/components/workspace/DirTree.vue";
  import ContextMenu from "@/components/workspace/ContextualMenu.vue";
  import NewFileModal from "@/components/workspace/NewFileModal.vue";
  import { createFile } from "@/api/project.js";
  import { buildTree } from "@/components/workspace/utils.js";

  export default {
    name: "SideBar",
    props: {
      files: Array,
      proj_id: String,
      currentFileId: String,
      editPermit: Boolean,
    },
    components: {
      DirTree,
      ContextMenu,
      NewFileModal,
    },
    data() {
      return {
        tree: {},
        //Context menu data
        menuFolderItems: [
          {
            label: "New File",
            action: (folder) => {
              console.log("New File in", folder);
              this.newFilePath = folder;
              console.log(this.newFilePath);
            },
          },
          //   {
          //     label: "Delete",

          //     action: (a) => {
          //       console.log("Folder Delete", a);
          //       alert("Folder Delete Not Implemented Yet");
          //     },
          //   },
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
        //Modal data
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
      console.log(this.files);
      let tree = buildTree(this.files);
      console.log(tree);
      this.tree = tree;
    },
  };
</script>
