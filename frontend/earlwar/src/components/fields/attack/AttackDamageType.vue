<template>
  <validation-provider
      v-slot="{ errors }"
      vid="AttackDamageType"
      name="AttackDamageType"
      ref="validation"
  >
    <v-select
        label="Damage Type"
        v-model="internalValue"
        :items="damages"
        :error-messages="errors"
        :disabled="isDisabled"
    ></v-select>
  </validation-provider>
</template>

<script>
  import BaseField from "@/components/fields/common/BaseField";

  export default {
    extends: BaseField,
    name: 'AttackDamageType',
    props: {
      value: String,
      item: {},
      required: {
        type: Boolean,
        default: false,
      },
    },

    methods: {
      convertType(val) {
        return val
      },
      disableCondition() {
        return this.item.AttackType === 'None';
      }
    },
    data() {
      return {
        lazyValue: this.value,
        damages: ["Physical", "Magic", "Chaos"],
      };
    },

  };
</script>