<template>
  <ul class="nav justify-content-between">
    <li class="nav-item">Project: {{ workspaceName }}</li>
    <li class="nav-item">#id: {{ workspaceId }}</li>
    <li class="nav-item">
      <ProjectSettingsModal
        :name="this.workspaceName"
        :id="this.workspaceId"
        :user="this.user"
        :shared_users="this.shared_users"
        :is_public="this.is_public"
        v-if="this.editPermit"
      />
    </li>
  </ul>
</template>

<script>
  import ProjectSettingsModal from "@/components/ProjectSettingsModal.vue";
  export default {
    name: "TopBar",
    components: { ProjectSettingsModal },
    props: {
      workspaceName: String,
      workspaceId: String,
      user: String,
      shared_users: Array,
      is_public: Boolean,
      editPermit: Boolean,
    },
  };
</script>
