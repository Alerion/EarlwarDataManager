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
              <v-row v-for="(parameter, index)  in ability.unpackedParameters" :key="index" align="center">
                <v-col md="5">
                  <v-select
                      label="Parameters"
                      :items="availableParameters"
                      v-model="ability.unpackedParameters[index].name"
                      @input="onChange(index, $event)"
                  ></v-select>
                </v-col>
                <v-col md="5">
                  <v-text-field
                      v-model="ability.unpackedParameters[index].value"
                      @input="onInput(index, $event)"
                  ></v-text-field>
                </v-col>
                <v-col md="2">
                  <v-icon
                      @click="removeField(index)"
                      color="error"
                  >
                    mdi-trash-can-outline
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
      fieldsFromValue(value) {
        const ability = {
          Id: value.Id,
        };
        ability.unpackedParameters = [];
        for (let key of Object.keys(value.Parameters)) {
          ability.unpackedParameters.push({
            name: key,
            value: value.Parameters[key],
          })
        }
        return ability
      },
      getAvailableParameters() {
        this.availableParameters = []
        for (let parameter of this.parameters) {
          this.availableParameters.push({
            text: parameter,
            value: parameter,
            disabled: this.value.Parameters[parameter] !== "undefined",
          });
        }
      },
      getValue() {
        const result = {
          Id: this.ability.Id,
        };
        result.Parameters = {}
        for (let parameter of this.ability.unpackedParameters) {
          result.Parameters[parameter.name] = parameter.value;
        }
        return result;
      },
      removeField(index) {
        this.ability.unpackedParameters.splice(index, 1);
        this.$emit('input', this.getValue());
        this.getAvailableParameters();
      },
      onInput(fieldIndex, value) {
        this.ability.unpackedParameters[fieldIndex].value = value;
        this.$emit('input', this.getValue());
        this.getAvailableParameters();

      },
      onChange(fieldIndex, value) {
        this.ability.unpackedParameters[fieldIndex].name = value;
        this.$emit('input', this.getValue());
      },

    },
    data() {
      return {
        parameters: [],
        availableParameters: [],
        ability: this.fieldsFromValue(this.value),
        show: true,
      }
    },
    mounted() {
      Api.item({'path': this.availableAbilities[this.ability.Id]})
        .then(
          response => {
            this.parameters = Object.keys(response.data.AbilitySpecial);
            this.getAvailableParameters();
          }
        )
    }
  }
</script>