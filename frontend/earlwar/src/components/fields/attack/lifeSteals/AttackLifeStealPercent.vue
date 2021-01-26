<template>
  <validation-provider
      v-slot="{ errors }"
      vid="AttackLifeStealPercent"
      name="AttackLifeStealPercent"
      rules="min_value:0|max_value:100"
      ref="validation"
  >
    <v-text-field
        v-model="internalValue"
        label="Life Steal Percent"
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
          Life Steal probability in percent 1 - 100 value
        </v-tooltip>
      </template>
    </v-text-field>
  </validation-provider>
</template>

<script>
  import BaseField from "@/components/fields/common/NumberField";

  export default {
    extends: BaseField,
    name: 'AttackLifeStealPercent'
  };
</script>