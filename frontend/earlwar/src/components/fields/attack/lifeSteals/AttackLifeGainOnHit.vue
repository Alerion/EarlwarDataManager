<template>
  <validation-provider
      v-slot="{ errors }"
      vid="AttackLifeGainOnHit"
      name="AttackLifeGainOnHit"
      ref="validation"
  >
    <v-text-field
        v-model="internalValue"
        label="Life Gain On Hit"
        default="0"
        type="number"
        step="0.1"
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
    name: 'AttackLifeGainOnHit'
  };
</script>