<template>
  <validation-provider
      v-slot="{ errors }"
      vid="ChaoticResistance"
      name="ChaoticResistance"
      rules="required"
      ref="validation"
  >
    <v-text-field
        v-model="internalValue"
        label="Chaotic Resistance"
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
    name: 'ChaoticResistance'
  };
</script>