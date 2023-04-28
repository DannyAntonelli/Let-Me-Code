<template>
  Side

  <!-- <div v-for="file_id in files" :key="file_id">
    {{ file_id }}
  </div> -->
  <DirTree :node="this.tree" :key="this.tree" :root="this" />
  <ContextMenu
    :items="menuItems"
    :position="menuPosition"
    :visible="menuVisible"
    :param="menuParam"
  />
</template>

<script>
  // declare interface File {
  //     cod: string,
  //     param: string
  // }
  // import { getFile } from "@/api/file.js";
  import DirTree from "@/components/workspace/DirTree.vue";
  import ContextMenu from "@/components/workspace/ContextualMenu.vue";

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
            // console.log("f", path.slice(1, i + 1));

            curr[path[i]] = {
              folderName: path.slice(0, i + 1).join("/") + "/",
            };
          }
          curr = curr[path[i]];
        }
      }
    }

    // console.log(tree[""]);
    tree["root"] = tree[""];
    delete tree[""];
    console.log(tree);
    return tree;
  }
  export default {
    name: "SideBar",
    props: {
      file_ids: Array,
    },
    components: {
      DirTree,
      ContextMenu,
    },
    data() {
      return {
        files: [],
        tree: {},
        menuFolderItems: [
          {
            label: "New File",
            action: (folder) => {
              //   this.showing = true;
              console.log("Item 1 clicked", folder);
              this.newFilePath = folder;
              console.log(this.newFilePath);
              //   let m = new Modal(document.querySelector("#newFileModal"));
              //   m.show();
            },
          },
          {
            label: "Delete",

            action: (a) => {
              console.log("Item 2 clicked", a);
              // let m = new Modal(document.querySelector("#newFileModal"));
              // m.show();
            },
          },
        ],
        menuFileItems: [
          {
            label: "Delete",
            action: (a) => console.log("File 2 clicked", a),
          },
        ],
        menuItems: this.menuFolderItems,
        menuPosition: { x: 0, y: 0 },
        menuVisible: false,
        menuParam: null,
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
    },
    async created() {
      // for (let file_id of this.file_ids) {
      //   console.log(file_id);
      //   console.log("aaa    ");
      //   let f = await getFile(file_id);
      //   // .then((response) => {
      //   //   this.files.push(response); // Race condition?
      //   // })
      //   // .catch((error) => {
      //   //   console.log(error);
      //   // });
      //   this.files.push(f.file);
      // }
      this.files = [
        { id: 1, name: "/file1", content: "", language: "py", project: 1 },
        { id: 2, name: "/file3", content: "", language: "py", project: 1 },
        {
          id: 3,
          name: "/folder/file2",
          content: "",
          language: "py",
          project: 1,
        },
        {
          id: 4,
          name: "/folder/file5",
          content: "",
          language: "py",
          project: 1,
        },
      ];
      console.log(this.files);
      let tree = buildTree(this.files);
      console.log(tree);
      this.tree = tree;
    },
  };
</script>
