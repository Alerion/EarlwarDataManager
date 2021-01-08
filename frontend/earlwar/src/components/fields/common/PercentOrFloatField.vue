<template>
  <div>
    <h4>{{title}}</h4>
    <div>
      <v-switch
          v-model="isPercent"
          label="interval/%"
      ></v-switch>
    </div>
    <div>
      <number-field
          v-if="isPercent"
          v-model="item[percentField]"
          :vid="percentField"
          :name="percentField"
          :label="percentField"
          rules="min_value:0|max_value:100"
      ></number-field>
      <min-max-field
          v-else
          :title="title"
          :min-field="minField"
          :max-field="maxField"
          :item="item"
          step="0.1"
      ></min-max-field>
    </div>
  </div>
</template>

<script>
  import NumberField from "@/components/fields/common/NumberField";
  import MinMaxField from "@/components/fields/common/MinMaxField";

  export default {
    name: "PercentOrFloatField",
    components: {MinMaxField, NumberField},
    props: {
      item: {},
      title: String,
      percentField: String,
      minField: String,
      maxField: String,
    },
    watch: {
      isPercent(val) {
        if (val) {
          this.item[this.minField] = null;
          this.item[this.maxField]  = null;
        } else {
          this.item[this.percentField]  = null
        }
      }
    },
    data() {
      const hasMinMax = typeof this.item[this.minField] !== "undefined" && typeof this.item[this.maxField] !== "undefined"
      const hasPercent = typeof this.item[this.percentField] !== "undefined"
      return {
        isPercent: hasPercent || (!hasMinMax && !hasMinMax)
      };
    },
  }
</script>