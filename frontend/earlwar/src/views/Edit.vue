<template v-if="type='Unit'">
  <editor :path="path"></editor>
</template>

<script>
  // @ is an alias to /src
  import Editor from "@/components/Editor";

  export default {
    name: 'Form',
    components: {
      Editor
    },
    computed: {
      path: function () {
        return this.$route.params.path
      },
      type: function () {
        return this.$route.params.type
      },
    },
  }
</script>
