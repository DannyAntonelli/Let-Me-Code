<template>
<ul class="nav justify-content-between">
    <li class="nav-item">
        Workspace name is {{ workspaceName }}
    </li>
    <li class="nav-item">
        #id is {{ workspaceId }}
    </li>
    <li class="nav-item">
        Settings
    </li>
</ul>
</template>

<script>
export default {
    name: 'TopBar',
    props: {
        workspaceName: String,
        workspaceId: String,
    }
}
</script>
