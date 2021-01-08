<template>
  <validation-provider
      v-slot="{ errors }"
      vid="AOEDamageType"
      name="AOEDamageType"
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
    name: 'AOEDamageType',
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
        return String(val)
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