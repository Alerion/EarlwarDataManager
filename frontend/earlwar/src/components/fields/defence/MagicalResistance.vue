<template>
  <validation-provider
      v-slot="{ errors }"
      vid="MagicalResistance"
      name="MagicalResistance"
      rules="required"
      ref="validation"
  >
    <v-text-field
        v-model="internalValue"
        label="Magical Resistance"
        default="0"
        type="number"
        required
        :error-messages="errors"
    >
    </v-text-field>
  </validation-provider>
</template>

<script>
  import BaseField from "@/components/fields/common/BaseField";

  export default {
    extends: BaseField,
    name: 'MagicalResistance'
  };
</script>