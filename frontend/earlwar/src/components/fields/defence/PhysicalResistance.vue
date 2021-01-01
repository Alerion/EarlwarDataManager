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
  import Field from "@/components/fields/common/Field";

  export default {
    extends: Field,
    name: 'PhysicalResistance'
  };
</script>