<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <sidebar />
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Earlvar data manager</v-toolbar-title>
    </v-app-bar>

    <v-main class="ml-10">
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
  import Sidebar from "@/components/Sidebar";
  export default {
    components: {Sidebar},
    data: () => ({ drawer: null }),
  }
</script>