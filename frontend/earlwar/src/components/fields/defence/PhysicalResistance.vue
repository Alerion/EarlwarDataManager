<template>
  <validation-provider
      v-slot="{ errors }"
      vid="PhysicalResistance"
      name="PhysicalResistance"
      rules="required"
      ref="validation"
  >
    <v-text-field
        v-model="internalValue"
        label="Physical Resistance"
        default="0"
        type="number"
        required
        :error-messages="errors"
    >
    </v-text-field>
  </validation-provider>
</template>

<script>
  import BaseField from "@/components/fields/common/NumberField";

  export default {
    extends: BaseField,
    name: 'PhysicalResistance'
  };
</script>