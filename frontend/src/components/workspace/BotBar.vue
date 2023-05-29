<template>
  <div class="text-start">
    <span class="">
      Language<strong>
        {{ this.file ? ": " + this.file.language : "" }}
      </strong></span
    >

    <span class="">
      <div class="dropdown">
        <button
          class="btn dropdown-toggle"
          type="button"
          data-bs-toggle="dropdown"
          aria-expanded="false"
          style="margin-left: 0; padding-left: 0"
        >
          Theme: <strong>{{ this.theme }}</strong>
        </button>
        <ul class="dropdown-menu">
          <li v-for="theme in this.themes" :key="theme">
            <a class="dropdown-item" @click="selectTheme(theme)">{{ theme }}</a>
          </li>
        </ul>
      </div>
    </span>
  </div>
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
