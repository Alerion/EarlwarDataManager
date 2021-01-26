<template>
  <validation-provider
      v-slot="{ errors }"
      vid="EfficiencyBlock"
      name="EfficiencyBlock"
      rules="min_value:0|max_value:75"
      ref="validation"
  >
    <v-text-field
        v-model="internalValue"
        label="Efficiency Block"
        default="0"
        type="number"
        step="1"
        :error-messages="errors"
    >
      <template v-slot:prepend>
        <v-tooltip
            top
        >
          <template v-slot:activator="{ on }">
            <v-icon v-on="on">
              mdi-percent
            </v-icon>
          </template>
          Efficiency block in percent 1 - 100 value
        </v-tooltip>
      </template>
    </v-text-field>
  </validation-provider>
</template>

<script>
  import BaseField from "@/components/fields/common/NumberField";

  export default {
    extends: BaseField,
    name: 'EfficiencyBlock'
  };
</script>