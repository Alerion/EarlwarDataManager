<template>
  <validation-provider
      v-slot="{ errors }"
      vid="AOEAOERadius"
      name="AOERadius"
      ref="validation"
  >
    <v-text-field
        v-model="internalValue"
        label="AOERadius"
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
  import BaseField from "@/components/fields/common/BaseField";

  export default {
    extends: BaseField,
    name: 'AOERadius'
  };
</script>