<template>
<!-- <div>
        <h1>Workspace</h1>
        <p>{{ $route.params.id }}</p>
        <p>{{ name }}</p>
        <p>{{ description }}</p>
        <p>{{ is_public }}</p>
        <p>{{ user }}</p>
        <p>{{ shared_users }}</p>
        <p>{{ file_ids }}</p>
    </div> -->
<div class="container text-center">
    <div class="row text-start">
        <TopBar :workspaceName='this.name' :workspaceId='this.id' />
    </div>
    <div class="row align-items-start">
        <div class="col-2">
            <SideBar :file_ids='this.file_ids' />
        </div>
        <div class="col-10">
            <CodeEditor />
        </div>
    </div>
    <div class="row">
        <BotBar />
    </div>
</div>
</template>

<script>
import {
    getProject
} from '@/api/project.js'
import CodeEditor from '@/components/workspace/CodeEditor.vue'
import TopBar from '@/components/workspace/TopBar.vue'
import BotBar from '@/components/workspace/BotBar.vue'
import SideBar from '@/components/workspace/SideBar.vue'

export default {
    name: 'Profile',
    components: {
        CodeEditor,
        TopBar,
        BotBar,
        SideBar,
    },
    data() {
        return {
            file_ids: [],
            description: '',
            id: '',
            is_public: false,
            name: '',
            shared_users: [],
            user: '',
        }
    },

    async created() {
        getProject(this.$route.params.id)
            .then(response => {
                console.log(response)
                this.file_ids = response.file_ids
                this.description = response.project.description
                this.id = response.project.id
                this.is_public = response.project.is_public
                this.name = response.project.name
                this.shared_users = response.project.shared_users
                this.user = response.project.user
            })
            .catch(error => {
                console.log(error)
            })
    }
}
</script>
