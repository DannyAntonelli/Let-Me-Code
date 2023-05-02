<template>
  <ul class="tree">
    <li v-for="(value, key) in this.node" :key="key">
      <div v-if="value.id === undefined && key != 'folderName'">
        <!--check if has id -> is a file and not a folder -->
        <span
          class="folder"
          @click="toggle(key)"
          @contextmenu.prevent="
            this.root.showMenu($event, false, value.folderName)
          "
        >
          {{ key }}
        </span>
        <dir-tree v-if="expanded[key]" :node="value" :root="this.root" />
      </div>
      <div v-if="!(value.id === undefined)">
        <span
          class="file"
          @contextmenu.prevent="this.root.showMenu($event, true, value)"
          @click="this.root.onFileClick(value)"
        >
          - {{ value.fileName }}
        </span>
      </div>
    </li>
  </ul>
</template>

<style scoped>
  ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
  }
  .folder {
    cursor: pointer;
  }
  .file {
    color: #666;
  }
  ul.tree {
    list-style-type: none;
    margin: 0;
    padding: 0;
    font-family: sans-serif;
    font-size: 14px;
    color: #333;
  }

  ul.tree li {
    padding-left: 1em;
    position: relative;
  }

  ul.tree li:before {
    content: "";
    position: absolute;
    left: -0.5em;
    top: 0.5em;
    border-left: 1px solid #ccc;
    border-bottom: 1px solid #ccc;
    height: calc(100% - 1em);
  }

  ul.tree li:last-child:before {
    border-left: none;
  }

  ul.tree li:after {
    content: "";
    position: absolute;
    left: -0.5em;
    top: 0.5em;
    border-left: 1px solid #ccc;
    border-top: 1px solid #ccc;
    height: 0.5em;
    width: 1em;
  }

  ul.tree li:last-child:after {
    border-left: none;
  }

  ul.tree li > div {
    position: relative;
    padding: 0.5em 0;
  }

  ul.tree li > div:before {
    content: "";
    position: absolute;
    left: -1.5em;
    top: 0.5em;
    border-left: 1px solid #ccc;
    border-bottom: 1px solid #ccc;
    height: calc(100% - 1em);
  }

  ul.tree li > div:last-child:before {
    border-left: none;
  }

  ul.tree li > div:after {
    content: "";
    position: absolute;
    left: -1.5em;
    top: 0.5em;
    border-left: 1px solid #ccc;
    border-top: 1px solid #ccc;
    height: 0.5em;
    width: 1em;
  }

  ul.tree li > div:last-child:after {
    border-left: none;
  }

  ul.tree li > div .toggle {
    display: inline-block;
    margin-right: 0.5em;
    width: 1.2em;
    height: 1.2em;
    line-height: 1.2em;
    text-align: center;
    cursor: pointer;
    font-weight: bold;
    color: #666;
    border-radius: 50%;
    border: 1px solid #ccc;
    background-color: #fff;
    transition: background-color 0.2s ease;
  }

  ul.tree li > div .toggle:hover {
    background-color: #eee;
  }

  ul.tree li > div .toggle.expanded {
    background-color: #ccc;
    color: #fff;
  }
</style>

<script>
  export default {
    name: "DirTree",
    props: {
      node: {},
      root: Object,
      onFileClick: Function,
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
