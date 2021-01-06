<template>
  <div>
    <h4>{{title}}</h4>
    <v-row>
      <v-col
          cols="12"
          md="5"
      >
        <field
            v-model="item[minField]"
            v-bind="$attrs"
            vid="Min"
            name="Min"
            label="Min"
            type="number"
            :rules="$attrs.rules + '|max_value:'+item[maxField]"
        ></field>
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
        <field
            v-model="item[maxField]"
            v-bind="$attrs"
            vid="Max"
            name="Max"
            label="Max"
            type="number"
            :rules="$attrs.rules + '|min_value:'+item[minField]"
        ></field>
      </v-col>
    </v-row>
  </div>
</template>

<script>
  import Field from "@/components/fields/common/Field";

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
    components: {Field}
  }
</script>