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
        :label="label"
        :type="type"
        :error-messages="errors"
        :disabled="isDisabled"
    >
    </v-text-field>
  </validation-provider>
</template>

<script>
  import BaseField from "@/components/fields/common/BaseField";

  export default {
    extends: BaseField,
    name: 'Field',
    props: {
      value: null,
      item: {},
      vid: String,
      name: String,
      rules: String,
      label: String,
      type: {
        type: String,
        default: "text",
      },
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
      disableCondition() {
        return this.disabled
      },
    }
  };
</script>