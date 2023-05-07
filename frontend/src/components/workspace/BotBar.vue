<template>
  <ul class="nav justify-content-between">
    <li class="nav-item">
      Language{{ this.file ? ": " + this.file.language : "" }}
    </li>
    <li class="nav-item">Font</li>
    <li class="nav-item">
      <div class="dropdown">
        <button
          class="btn dropdown-toggle"
          type="button"
          data-bs-toggle="dropdown"
          aria-expanded="false"
        >
          Theme: {{ this.theme }}
        </button>
        <ul class="dropdown-menu">
          <li v-for="theme in this.themes" :key="theme">
            <a class="dropdown-item" @click="selectTheme(theme)">{{ theme }}</a>
          </li>
        </ul>
      </div>
    </li>
  </ul>
</template>

<script>
  export default {
    name: "BotBar",
    props: {
      file: Object,
      theme: String,
    },
    data() {
      return {
        themes: ["vs", "vs-dark", "hc-black", "hc-light"],
      };
    },
    methods: {
      selectTheme(theme) {
        this.$emit("theme-changed", theme);
      },
    },
  };
</script>
