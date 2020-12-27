<template v-if="type='Unit'">
  <unit-form :path="path"></unit-form>
</template>

<script>
  // @ is an alias to /src
  import UnitForm from '@/components/UnitForm.vue'

  export default {
    name: 'Form',
    components: {
      UnitForm
    },
    computed: {
      path: function () {
        return this.$route.params.path
      },
      type: function () {
        return this.$route.params.type
      },
    }
  }
</script>
