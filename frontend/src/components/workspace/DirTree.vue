<template>
  <!-- <ul>
    <li v-for="(value, key) in this.node" :key="key">
      <span>{{ key }} </span>
      <directory-tree
        v-if="value && value.constructor === Object"
        :tree="{ a: 'b' }"
      />
    </li>
  </ul> -->
  <ul class="tree">
    <li v-for="(value, key) in this.node" :key="key">
      <!-- aaa {{ key }} {{ value }} -->
      <div v-if="isObject(value)">
        <span
          class="folder"
          @click="toggle(key)"
          @auxclick="contextual_menu(key)"
        >
          {{ key }}
        </span>
        <dir-tree v-if="expanded[key]" :node="value" />
      </div>
      <div v-else>
        <span class="file"> f {{ value }} </span>
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
  //   import $ from "jquery";

  export default {
    name: "DirTree",
    props: {
      node: {},
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
