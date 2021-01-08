<template>
  <min-max-field
    title="Damage"
    min-field="DamageMin"
    max-field="DamageMax"
    :item="item"
    :disabled="disabledCondition"
    step="0.1"
  ></min-max-field>
</template>

<script>
  import MinMaxField from "@/components/fields/common/MinMaxField";
  export default {
    name: "AttackDamage",
    components: {MinMaxField},
    props: {
      item: Object,
    },
    computed: {
      disabledCondition() {
        return this.item.AttackType === 'None';
      }
    }
  }
</script>