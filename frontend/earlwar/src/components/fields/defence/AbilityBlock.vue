<template>
  <validation-provider
      v-slot="{ errors }"
      vid="AbilityBlock"
      name="AbilityBlock"
      rules="min_value:0|max_value:100"
      ref="validation"
  >
    <v-text-field
        v-model="internalValue"
        label="Ability Block"
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
          Ability block probability in percent 1 - 100 value
        </v-tooltip>
      </template>
    </v-text-field>
  </validation-provider>
</template>

<script>
  import Field from "@/components/fields/common/Field";

  export default {
    extends: Field,
    name: 'AbilityBlock'
  };
</script>