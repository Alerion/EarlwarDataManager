<template>
  <v-card
      class="mt-10"
      width="1024"
  >
    <v-card-title>Abilities</v-card-title>
    <v-card-text>
      <div v-for="(ability, index) in abilities" :key="ability.Id">
        <ability
            v-model="abilities[index]"
            :available-abilities="availableAbilities"
            @close="deleteField(index)"
        ></ability>
      </div>
    </v-card-text>
    <v-card-actions>
      <v-btn
          color="info"
          text
          small
          @click="addField()"
      >
        <v-icon small class="mr-1">mdi-plus</v-icon>
        Add another
      </v-btn>
    </v-card-actions>
  </v-card>
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
    methods: {
      addField() {
        this.abilities.push({Id: null, Parameters: {}});
      },
      deleteField(index) {
        this.abilities.splice(index,1);
      }
    },
    mounted() {
      Api.abilities()
        .then(
          response => {
            for (let item of response.data.data) {
              this.availableAbilities[item.name.split('.')[0]] = item.href;
            }
          }
        )
    }
  }
</script>