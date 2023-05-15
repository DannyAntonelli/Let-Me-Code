<template>
  <div class="row justify-content-between">
    <div class="col-10" style="margin: auto">
      Project #{{ workspaceId }}: {{ workspaceName }}
    </div>
    <div class="col-2">
      <ProjectSettingsModal
        :name="this.workspaceName"
        :id="this.workspaceId"
        :user="this.user"
        :shared_users="this.shared_users"
        :is_public="this.is_public"
        v-if="this.editPermit"
      />
    </div>
  </div>
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
