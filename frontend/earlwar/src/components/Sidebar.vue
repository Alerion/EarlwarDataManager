<template>
  <v-treeview
      :items="items"
      activatable
      :active="active()"
      :open="open()"
      item-key="name"
  >
    <template v-slot:prepend="{ item, open }">
      <v-icon v-if="item.children">
        {{ open ? 'mdi-folder-open' : 'mdi-folder' }}
      </v-icon>
      <v-icon v-else>
        mdi-code-json
      </v-icon>
    </template>
    <template v-slot:label="{ item }">
      <router-link
          :to="{ name: 'Folder', params: { path: item.href }}"
          v-if="item.children"
      >
        <b v-if="!item.depth">{{ item.name }}</b>
        <template v-else>{{ item.name }}</template>
      </router-link>
      <router-link
          :to="{
            name: 'Edit',
            params: { path: item.href, type: item.type }
          }"
          v-else
      >
        {{ item.name }}
      </router-link>
    </template>
  </v-treeview>
</template>

<script>
  import Api from '@/api/api'

  export default {
    name: "Sidebar",
    data() {
      return {
        items: [],
        tree: []
      }
    },
    methods: {
      open() {
        return this.$route.params.path ? this.$route.params.path.split('\\') : []
      },
      active() {
        return [this.open()[this.open().length - 1]]
      }
    },
    created() {
      Api.tree()
        .then(
          response => {
            this.items = response.data.items;
          }
        )
    }
  }
</script>


<style scoped>
  nav a {
    text-decoration: none;
    color: inherit;
  }
</style>