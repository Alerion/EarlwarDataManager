<template>
  <v-row>
    <v-col
        cols="12"
        md="4"
    >
      <slot name="1-col"></slot>
    </v-col>

    <v-col
        cols="12"
        md="4"
    >
      <slot name="2-col"></slot>
    </v-col>

    <v-col
        cols="12"
        md="4"
    >
      <slot name="3-col"></slot>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    name: "Row"
  }
</script>