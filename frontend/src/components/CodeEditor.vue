<template>
    <div id='code-editor' style='height: 500px'></div>
</template>

<script>
import loader from '@monaco-editor/loader';

export default {
    name: 'CodeEditor',
    async mounted() {
        const editorOptions = {
            language: 'python',
        }
        loader.init().then((monaco) => {
            monaco.editor.create(document.getElementById('code-editor'), editorOptions);
        });
    }
}
</script>
