<template>
  <ul class="tree">
    <li v-for="(value, key) in this.node" :key="key">
      <div v-if="isObject(value)">
        <span
          class="folder"
          @click="toggle(key)"
          @contextmenu.prevent="showMenu($event, false, key)"
        >
          {{ key }}
        </span>
        <dir-tree v-if="expanded[key]" :node="value" />
      </div>
      <div v-else>
        <span class="file" @contextmenu.prevent="showMenu($event, true, key)">
          f {{ value }}
        </span>
      </div>
    </li>
  </ul>
  <ContextMenu
    :items="menuItems"
    :position="menuPosition"
    :visible="menuVisible"
    :file="menuFile"
    :objName="menuObjName"
    :param="menuParam"
  />
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
  import ContextMenu from "@/components/workspace/ContextualMenu.vue";
  export default {
    name: "DirTree",
    props: {
      node: {},
    },
    data() {
      return {
        expanded: {},
        menuFolderItems: [
          {
            label: "New File",
            action: (a) => console.log("Item 1 clicked", a),
          },
          {
            label: "Delete",
            action: (a) => console.log("Item 2 clicked", a),
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
    components: {
      ContextMenu,
    },

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
  };
</script>
