<template>
  Side

  <!-- <div v-for="file_id in files" :key="file_id">
    {{ file_id }}
  </div> -->
  <DirTree :node="this.tree" :key="this.tree" />
</template>

<script>
  // declare interface File {
  //     cod: string,
  //     param: string
  // }
  // import { getFile } from "@/api/file.js";
  import DirTree from "@/components/workspace/DirTree.vue";

  function buildTree(files) {
    let tree = {};
    for (let file of files) {
      let path = ("/" + file.name).split("/");
      let curr = tree;
      for (let i = 0; i < path.length; i++) {
        if (i == path.length - 1) {
          curr[path[i]] = file.name;
        } else {
          if (curr[path[i]] == undefined) {
            // let k = path[i] != "" ? path[i] : "root";
            curr[path[i]] = {};
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
    },
    data() {
      return {
        files: [],
        tree: {},
      };
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
        { id: 1, name: "file1", content: "", language: "py", project: 1 },
        { id: 2, name: "file3", content: "", language: "py", project: 1 },
        {
          id: 3,
          name: "folder/file2",
          content: "",
          language: "py",
          project: 1,
        },
        {
          id: 4,
          name: "folder/file5",
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

    methods: {},
  };
</script>
