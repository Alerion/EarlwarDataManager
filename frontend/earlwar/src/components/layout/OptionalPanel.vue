<template>
  <v-expansion-panels>
    <v-expansion-panel>
      <v-expansion-panel-header
        :color="color"
      >
        <slot name="header"></slot>
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        <slot name="content"></slot>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
  export default {
    name: "Panel",
    props: {
      active: {
        type: Boolean,
        default: false,
      },
    },
    computed: {
      color() {
        return this.active ? 'success' : null
      }
    }
  }
</script>