<template>
  <v-card
      class="mx-auto mt-5"
  >
    <v-system-bar
        color="teal darken-3"
        dark
    >
      <v-spacer>{{ability.Id}}</v-spacer>
      <v-icon
          @click="show = !show"
      >
        mdi-window-minimize
      </v-icon>

      <v-icon>mdi-close</v-icon>
    </v-system-bar>
    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          <v-row>
            <v-col md="3">
              <v-text-field
                  disabled
                  label="Id"
                  v-model="ability.Id"
              ></v-text-field>
            </v-col>
            <v-col md="9">
              <v-row v-for="(value, name)  in ability.Parameters" :key="name" align="center">
                <v-col md="5">
                  <v-select
                      label="Parameters"
                      :items="parameters"
                      :value="name"
                  ></v-select>
                </v-col>
                <v-col md="5">
                  <v-text-field
                      v-model="ability.Parameters[name]"
                  ></v-text-field>
                </v-col>
                <v-col md="2">
                  <v-icon
                      @click="removeField(name)"
                      color="error"
                  >mdi-trash-can-outline
                  </v-icon>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
  import Api from "@/api/api"

  export default {
    name: "Ability",
    props: {
      value: Object,
      availableAbilities: Object,
    },
    methods: {
      getValue() {
        return this.ability;
      },
      removeField(name) {
        delete this.ability.Parameters[name];
        this.ability = Object.assign({}, this.ability)
        this.$emit('input', this.getValue());
      }
    },
    data() {
      return {
        parameters: [],
        ability: this.value,
        show: true,
      }
    },
    mounted() {
      Api.item({'path': this.availableAbilities[this.ability.Id]})
        .then(
          response => {
            this.parameters = Object.keys(response.data.AbilitySpecial);
          }
        )
    }
  }
</script>