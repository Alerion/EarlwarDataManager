<template>
  <validation-provider
      v-slot="{ errors }"
      :vid="vid"
      :name="name"
      :rules="rules"
      ref="validation"
  >
    <v-text-field
        v-bind="$attrs"
        v-model="internalValue"
        type="number"
        step="1"
        :label="label"
        :error-messages="errors"
        :disabled="isDisabled"
    >
      <template v-slot:prepend>
        <slot name="icons"></slot>
      </template>
    </v-text-field>
  </validation-provider>
</template>

<script>
  import BaseField from "@/components/fields/common/BaseField";

  export default {
    extends: BaseField,
    name: 'NumberField',
    props: {
      value: Number,
      item: {},
      vid: String,
      name: String,
      label: String,
      rules: String,
      disabled: {
        type: Boolean,
        default: false,
      },
      required: {
        type: Boolean,
        default: false,
      },
    },
    methods: {
      convertType(val) {
        return Number(val)
      },
      disableCondition() {
        return this.disabled
      },
    }
  };
</script>