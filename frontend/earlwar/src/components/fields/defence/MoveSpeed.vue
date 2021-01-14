<template>
  <validation-provider
      v-slot="{ errors }"
      vid="MoveSpeed"
      name="MoveSpeed"
      rules="{'required':!isDisabled}"
      ref="validation"
  >
    <v-select
        label="Move speed"
        v-model="internalValue"
        :disabled="isDisabled"
        :items="speed"
        :error-messages="errors"
    ></v-select>
  </validation-provider>
</template>

<script>
  import BaseField from "@/components/fields/common/BaseField";

  export default {
    extends: BaseField,
    name: 'MoveSpeed',
    props: {
      value: String,
      item: {},
      required: {
        type: Boolean,
        default: false,
      },
    },
    methods: {
      convertType: function (val) {
        return String(val)
      },
      disableCondition() {
        return this.item.IsTower;
      }
    },
    data() {
      return {
        lazyValue: this.value,
        speed: ["None", "Slow", "Normal", "Fast"],
      };
    },

  };
</script>