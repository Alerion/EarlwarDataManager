<template>
  <validation-provider
      v-slot="{ errors }"
      vid="AttackType"
      name="AttackType"
      rules="required"
      ref="validation"
  >
    <v-select
        label="Type"
        v-model="internalValue"
        :items="attacks"
        :error-messages="errors"
    ></v-select>
  </validation-provider>
</template>

<script>
  import BaseField from "@/components/fields/common/BaseField";

  export default {
    extends: BaseField,
    name: 'AttackType',
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
        attacks: ["None", "Melee", "Arrow", "Cannonball"],
      };
    },

  };
</script>