<template>
  <validation-provider
      v-slot="{ errors }"
      vid="AttackRange"
      name="AttackRange"
      ref="validation"
  >
    <v-select
        label="Range"
        v-model="internalValue"
        :items="ranges"
        :error-messages="errors"
        :disabled="isDisabled"
    ></v-select>
  </validation-provider>
</template>

<script>
  import BaseField from "@/components/fields/common/BaseField";

  export default {
    extends: BaseField,
    name: 'AttackRange',
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
      },
      disableCondition() {
        return this.item.AttackType === 'None' || this.item.AttackType === 'Melee';
      }
    },
    data() {
      return {
        lazyValue: this.value,
        ranges: ["Close", "Middle", "Far"],
      };
    },

  };
</script>