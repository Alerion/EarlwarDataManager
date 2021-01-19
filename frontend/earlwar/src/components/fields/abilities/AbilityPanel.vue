<template>
  <div>
    <div v-for="(ability, index) in abilities" :key="ability.Id">
      <ability v-model="abilities[index]" :available-abilities="availableAbilities"></ability>
      {{abilities[index]}}
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
        availableAbilities: {},
      }
    },
    mounted() {
      Api.abilities()
        .then(
          response => {
            for (let item of response.data.data) {
              this.availableAbilities[item.name.split('.')[0]] =  item.href;
            }
          }
        )
    }
  }
</script>