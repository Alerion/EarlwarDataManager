<template>
  <validation-provider
      v-slot="{ errors }"
      vid="CritMultiplier"
      name="CritMultiplier"
      rules="min_value:1"
      ref="validation"
  >
    <v-text-field
        v-model="internalValue"
        label="Crit Multiplier"
        default="1"
        type="number"
        step="0.1"
        required
        :error-messages="errors"
    >
      <template v-slot:prepend>
        <v-tooltip
            top
        >
          <template v-slot:activator="{ on }">
            <v-icon v-on="on">
              mdi-multiplication
            </v-icon>
          </template>
          It's multiplier for the value of Crit Attack
        </v-tooltip>
      </template>
    </v-text-field>
  </validation-provider>
</template>

<script>
  import BaseField from "@/components/fields/common/NumberField";

  export default {
    extends: BaseField,
    name: 'CritMultiplier'
  };
</script>