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

      <v-icon
        @click="close"
      >mdi-close</v-icon>
    </v-system-bar>
    <v-expand-transition>
      <div v-show="show">
        <v-card-text>
          <v-row>
            <v-col md="3">
              <v-autocomplete
                  :disabled="ability.Id !== null"
                  label="Id"
                  v-model="ability.Id"
                  :items="Object.keys(availableAbilities)"
                  @input="onChangeId()"
              ></v-autocomplete>
            </v-col>
            <v-col md="9">
              <v-row v-for="(parameter, index)  in ability.unpackedParameters" :key="index" align="center">
                <v-col md="5">
                  <validation-provider
                      v-slot="{ errors }"
                      ref="validation"
                      rules="required"
                  >
                    <v-select
                        label="Parameters"
                        :items="availableParameters"
                        v-model="ability.unpackedParameters[index].name"
                        @input="onChange(index, $event)"
                        :error-messages="errors"
                    ></v-select>
                  </validation-provider>
                </v-col>
                <v-col md="5">
                  <validation-provider
                      v-slot="{ errors }"
                      ref="validation"
                      rules="required"
                  >
                    <v-text-field
                        v-model="ability.unpackedParameters[index].value"
                        @input="onInput(index, $event)"
                        :error-messages="errors"
                    ></v-text-field>
                  </validation-provider>
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
    watch: {
      parametersInUse: function () {
        this.getAvailableParameters();
      },
    },
    methods: {
      getAvailableParameters() {
        this.availableParameters = []
        for (let parameter of this.parameters) {
          this.availableParameters.push({
            text: parameter,
            value: parameter,
            disabled: this.parametersInUse.has(parameter),
          });
        }
      },
      fieldsFromValue(value) {
        const ability = {
          Id: value.Id,
        };
        ability.unpackedParameters = [];
        if (value.Parameters === undefined) {
          return ability;
        }
        for (let key of Object.keys(value.Parameters)) {
          ability.unpackedParameters.push({
            name: key,
            value: value.Parameters[key],
          })
        }
        return ability
      },
      getValue() {
        const result = {
          Id: this.ability.Id,
        };
        result.Parameters = {}
        for (let parameter of this.ability.unpackedParameters) {
          result.Parameters[parameter.name] = parameter.value;
        }
        this.parametersInUse = new Set(Object.keys(result.Parameters));
        return result;
      },
      removeField(index) {
        this.ability.unpackedParameters.splice(index, 1);
        this.$emit('input', this.getValue());
      },
      addField() {
        this.ability.unpackedParameters.push({name: null, value: null});
      },
      onInput(fieldIndex, value) {
        this.ability.unpackedParameters[fieldIndex].value = value;
        this.$emit('input', this.getValue());

      },
      onChange(fieldIndex, value) {
        this.ability.unpackedParameters[fieldIndex].name = value;
        this.$emit('input', this.getValue());
      },
      onChangeId() {
        this.$emit('input', this.getValue());
      },
      close() {
        if (confirm('Are you sure?')) {
          this.$emit('close');
        }
      }

    },
    data() {
      return {
        parameters: [],
        parametersInUse: new Set(this.value.Parameters === undefined ? [] : Object.keys(this.value.Parameters)),
        availableParameters: [],
        ability: this.fieldsFromValue(this.value),
        show: true,
      }
    },
    mounted() {
      if (this.ability.Id === null) {
        return;
      }
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