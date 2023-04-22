<template>
  Side
  <div v-for="file_id in files" :key="file_id">
    {{ file_id }}
  </div>
</template>

<script>
  // declare interface File {
  //     cod: string,
  //     param: string
  // }
  import { getFile } from "@/api/file.js";

  export default {
    name: "SideBar",
    props: {
      file_ids: Array,
    },
    data() {
      return {
        files: [],
      };
    },

    async mounted() {
      for (let file_id of this.file_ids) {
        console.log(file_id);
        console.log("aaa    ");
        getFile(file_id)
          .then((response) => {
            this.files.push(response);
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  };
</script>
