<template>
  <validation-provider
      v-slot="{ errors }"
      vid="MoveSpeed"
      name="MoveSpeed"
      rules="required"
      ref="validation"
  >
    <v-select
        label="Move speed"
        v-model="internalValue"
        :disabled="item.IsTower"
        :items="speed"
        :error-messages="errors"
    ></v-select>
  </validation-provider>
</template>

<script>
  import Field from "@/components/fields/common/Field";

  export default {
    extends: Field,
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
      type: function (val) {
        return String(val)
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