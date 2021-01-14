<template>
  <div>
    <div v-for="ability in abilities" :key="ability.Id">
      <ability :ability="ability" :available-abilities="availableAbilities"></ability>
    </div>
  </div>
</template>

<script>
  import Ability from "@/components/fields/abilities/Ability";
  import Api from "@/api/api"

  export default {
    name: "AbilityPanel",
    components: {Ability},
    props: {
      abilities: Array,
    },
    data: function () {
      return {
        availableAbilities: {}
      }
    },
    mounted() {
      Api.abilities()
        .then(
          response => {
            this.availableAbilities = response.data.data;
          }
        )
    }
  }
</script>

<style scoped>

</style>