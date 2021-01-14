<template>
  <v-card
      class="mx-auto mt-5"
  >
    <v-system-bar
        color="teal darken-3"
        dark
    >
      <v-spacer>{{ability.Id}}</v-spacer>
      <v-icon
          @click="show = !show"
      >
        mdi-window-minimize
      </v-icon>

      <v-icon>mdi-close</v-icon>
    </v-system-bar>
    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          <v-row>
            <v-col md="3">
              <v-text-field
                  disabled
                  label="Id"
                  v-model="ability.Id"
              ></v-text-field>
            </v-col>
            <v-col md="9">
              <v-row v-for="(value, name)  in ability.Parameters" :key="name">
                <v-col md-5>{{name}}</v-col>
                <v-col md-5>
                  <v-text-field
                    v-model="ability.Parameters[name]"
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
          {{ability}}
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
  export default {
    name: "Ability",
    props: {
      ability: Object,
      availableAbilities: Array
    },
    data: () => ({
      show: true,
    })
  }
</script>

<style scoped>

</style>