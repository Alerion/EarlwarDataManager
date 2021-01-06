<template>
  <validation-provider
      v-slot="{ errors }"
      vid="AttackSpeed"
      name="AttackSpeed"
      ref="validation"
  >
    <v-text-field
        v-model="internalValue"
        label="Attack Speed"
        default="0"
        type="number"
        step="1"
        :error-messages="errors"
        :disabled="isDisabled"
    >
      <template v-slot:prepend>
        <template v-slot:activator="{ on }">
            <span v-on="on">
              attack/S
            </span>
        </template>
      </template>
    </v-text-field>
  </validation-provider>
</template>

<script>
  import BaseField from "@/components/fields/common/BaseField";

  export default {
    extends: BaseField,
    name: 'AttackSpeed',
    methods: {
      disableCondition() {
        return this.item.AttackType === 'None';
      }
    },
  };
</script>