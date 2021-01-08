<template>
    <percent-or-float-field
      :item="item"
      title="Damage"
      percent-field="DamagePercent"
      min-field="DamageMin"
      max-field="DamageMax"
  ></percent-or-float-field>
</template>

<script>
  import PercentOrFloatField from "@/components/fields/common/PercentOrFloatField";
  export default {
    name: "PenetrationChaos",
    components: {PercentOrFloatField}
  }
</script>

<style scoped>

</style>