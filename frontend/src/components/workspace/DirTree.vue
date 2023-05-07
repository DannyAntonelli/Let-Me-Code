<template>
  <ul v-if="true" class="tree">
    <li v-for="(value, key) in this.node" :key="key">
      <div
        v-if="value.id === undefined && key != 'folderName'"
        class="justify-content-start text-left"
      >
        <!--check if has id -> is a file and not a folder -->
        <p
          class="folder"
          @click="toggle(key)"
          @contextmenu.prevent="
            this.root.showMenu($event, false, value.folderName)
          "
        >
          <font-awesome-icon
            icon="fa-regular fa-folder-open"
            v-if="expanded[key]"
          />
          <font-awesome-icon
            icon="fa-regular fa-folder"
            v-if="!expanded[key]"
          />

          {{ key }}
        </p>
        <dir-tree v-if="expanded[key]" :node="value" :root="this.root" />
      </div>
      <div v-if="!(value.id === undefined)">
        <p
          class="file"
          @contextmenu.prevent="this.root.showMenu($event, true, value)"
          @click="this.root.onFileClick(value)"
          v-bind:class="{ 'open-file': value.id === this.root.currentFileId }"
        >
          {{ value.fileName }}
          <font-awesome-icon
            icon="fa-solid fa-circle"
            style="color: #ce1c1c"
            v-if="!value.saved"
          />
        </p>
      </div>
    </li>
  </ul>
  <!-- </div> -->
</template>
<style>
  .tree,
  .tree ul {
    margin: 0;
    padding: 0;
    list-style: none;
  }
  .tree ul {
    margin-left: 1em;
    position: relative;
  }
  .tree ul ul {
    margin-left: 0.5em;
  }
  .tree ul:before {
    content: "";
    display: block;
    width: 0;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    border-left: 1px solid;
  }
  .tree li {
    margin: 0;
    padding: 0 1em;
    line-height: 2em;
    color: #369;
    font-weight: 700;
    position: relative;
  }
  .tree ul li:before {
    content: "";
    display: block;
    width: 10px;
    height: 0;
    border-top: 1px solid;
    margin-top: -1px;
    position: absolute;
    top: 1em;
    left: 0;
  }
  .tree ul li:last-child:before {
    background: #fff;
    height: auto;
    top: 1em;
    bottom: 0;
  }
  .indicator {
    margin-right: 5px;
  }
  .tree li a {
    text-decoration: none;
    color: #369;
  }
  .tree li button,
  .tree li button:active,
  .tree li button:focus {
    text-decoration: none;
    color: #369;
    border: none;
    background: transparent;
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
    outline: 0;
  }
  .folder {
    cursor: pointer;
    text-align: start;
  }
  .file {
    /* color: #666; */
    text-align: start;
  }
  .open-file {
    color: #19eeae;
  }
</style>

<script>
  export default {
    name: "DirTree",
    props: {
      node: {},
      root: Object,
      onFileClick: Function,
      currentFileId: String,
    },
    data() {
      return {
        expanded: {},
      };
    },
    components: {},

    async created() {
      console.log("mounted");
      console.log(JSON.stringify(this.node));
    },

    methods: {
      isObject(val) {
        return typeof val === "object";
      },

      toggle(key) {
        this.expanded[key] = !this.expanded[key];
      },
    },
  };
</script>
