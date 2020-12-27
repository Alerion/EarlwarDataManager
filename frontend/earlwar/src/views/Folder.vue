<template>
  <Table :path="path"/>
</template>

<script>
  // @ is an alias to /src
  import Table from '@/components/Table.vue'

  export default {
    name: 'Folder',
    components: {
      Table
    },
    computed: {
      path: function () {
        return this.$route.params.path
      }
    }
  }
</script>
