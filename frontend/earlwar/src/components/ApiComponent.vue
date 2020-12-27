<script>
  export default {
    name: "ApiComponent",
    props: ['path'],
    methods: {
      updateData() {
        //not implemented
      },
    },
    watch: {
      path(to, from) {
        if (to !== from) {
          this.updateData()
        }
      }
    },
    mounted() {
      this.updateData()
    }
  }
</script>