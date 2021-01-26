<template>
  <validation-provider
      v-slot="{ errors }"
      vid="MaxHealth"
      name="MaxHealth"
      rules="required|min_value:0.1"
      ref="validation"
  >
    <v-text-field
        v-model="internalValue"
        label="Max HP"
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
          It's multiplier for the reference HP
        </v-tooltip>
      </template>
    </v-text-field>
  </validation-provider>
</template>

<script>
  import BaseField from "@/components/fields/common/NumberField";

  export default {
    extends: BaseField,
    name: 'MaxHP'
  };
</script>