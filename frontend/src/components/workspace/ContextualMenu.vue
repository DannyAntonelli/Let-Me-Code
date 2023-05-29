<template>
  <div
    class="context-menu"
    id="side-bar-context-menu"
    v-show="visible"
    :style="{ top: position.y + 'px', left: position.x + 'px' }"
  >
    <ul>
      <li
        v-for="(item, index) in items"
        :key="index"
        @click="handleItemClick(item.action)"
      >
        {{ item.label }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "ContextMenu",

  props: {
    items: {
      type: Array,
      required: true,
    },
    position: {
      type: Object,
      required: true,
    },
    visible: {
      type: Boolean,
      required: true,
    },
    param: {
      type: Object,
    },
  },
  methods: {
    handleItemClick(action) {
      if (typeof action === "function") {
        action(this.param);
      }
    },
  },
  async mounted() {
    // on dismiss
    let contextMenu = document.getElementById("side-bar-context-menu");
    document.addEventListener("click", (e) => {
      if (!contextMenu.contains(e.target)) {
        this.$emit("close-context");
      }
    });
  },
};
</script>

<style scoped>
.context-menu {
  position: absolute;
  z-index: 100;
  background-color: white;
  border: 1px solid #ccc;
  width: 120px;
}

.context-menu ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.context-menu li {
  padding: 5px 10px;
  cursor: pointer;
}
</style>
