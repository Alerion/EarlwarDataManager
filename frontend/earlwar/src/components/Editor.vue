<template v-if="type='Unit'">
  <unit-form :path="this.path" :item="item"></unit-form>
</template>
<script>
  import Api from '@/api/api'
  import ApiComponent from "@/components/ApiComponent";
  import UnitForm from "@/components/UnitForm";

  export default {
    components: {UnitForm},
    extends: ApiComponent,
    name: "Editor",
    data() {
      return {
        item: {},
      }
    },
    methods: {
      updateData() {
        Api.item({'path': this.path})
          .then(
            response => {
              this.item = response.data;
            }
          )
      },
    }
  }
</script>