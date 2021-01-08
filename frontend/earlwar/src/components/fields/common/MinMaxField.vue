<template>
  <div>
    <h4>{{title}}</h4>
    <v-row>
      <v-col
          cols="12"
          md="5"
      >
        <number-field
            v-model="item[minField]"
            v-bind="$attrs"
            vid="Min"
            name="Min"
            label="Min"
            :rules="minRules"
        ></number-field>
      </v-col>
      <v-col
          cols="12"
          md="2"
          align-self="center"
      >
        <div class="text-center">—</div>
      </v-col>
      <v-col
          cols="12"
          md="5"
      >
        <number-field
            v-model="item[maxField]"
            v-bind="$attrs"
            vid="Max"
            name="Max"
            label="Max"
            :rules="maxRules"
        ></number-field>
      </v-col>
    </v-row>
  </div>
</template>

<script>
  import NumberField from "@/components/fields/common/NumberField";

  export default {
    props: {
      item: {},
      minField: String,
      maxField: String,
      title: String,
      disabled: {
        type: Boolean,
        default: false,
      },
    },
    name: "MinMaxField",
    components: {NumberField},
    computed: {
      minRules() {
        if (this.item[this.maxField] == null) {
          return;
        }
        return this.rules(`max_value:${this.item[this.maxField]}`)
      },
      maxRules() {
        if (this.item[this.minField] == null) {
          return;
        }
        return this.rules(`min_value:${this.item[this.minField]}`)
      },
    },
    methods: {
      rules(rules) {
        if (typeof this.$attrs.rules === String) {
          return `${this.$attrs.rules}|${rules}`;
        }
        return rules;
      }
    }
  }
</script>