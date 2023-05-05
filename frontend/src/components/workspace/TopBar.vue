<template>
  <ul class="nav justify-content-between">
    <li class="nav-item">Project: {{ workspaceName }}</li>
    <li class="nav-item">#id: {{ workspaceId }}</li>
    <!-- <li class="nav-item">Settings</li> -->
  </ul>
</template>

<script>
  export default {
    name: "TopBar",
    props: {
      workspaceName: String,
      workspaceId: String,
    },
  };
</script>
