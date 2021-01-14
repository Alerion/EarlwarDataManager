<template>
  <div>
    <h4>Physical</h4>
    <v-row>
      <v-col md="5">
        <number-field
            v-model="item.PenetrationPhysical"
            vid="PenetrationPhysical"
            name="PenetrationPhysical"
            label="Float"
            rules="min_value:0"
        ></number-field>
      </v-col>
      <v-col md="5">
        <number-field
            v-model="item.PenetrationPhysicalPercent"
            vid="PenetrationPhysicalPercent"
            name="PenetrationPhysicalPercent"
            label="Percent"
            rules="min_value:0|max_value:100"
        >
          <template v-slot:icons>
            <v-tooltip
                top
            >
              <template v-slot:activator="{ on }">
                <v-icon v-on="on">
                  mdi-percent
                </v-icon>
              </template>
              Physical Percent 1 - 100 value
            </v-tooltip>
          </template>
        </number-field>
      </v-col>
    </v-row>
  </div>
</template>

<script>
  import NumberField from "@/components/fields/common/NumberField";

  export default {
    name: 'PenetrationPhysical',
    components: {NumberField},
    props: {
      item: {},
    },
  };
</script>