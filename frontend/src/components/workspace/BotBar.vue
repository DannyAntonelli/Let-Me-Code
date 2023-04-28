<template>
  <ul class="nav justify-content-between">
    <li class="nav-item">
      Language{{ this.file ? ": " + this.file.language : "" }}
    </li>
    <li class="nav-item">Font</li>
    <li class="nav-item">Theme</li>
  </ul>
</template>

<script>
  export default {
    name: "BotBar",
    props: {
      file: Object,
    },
  };
</script>
