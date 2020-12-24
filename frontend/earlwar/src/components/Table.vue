<template>
  <v-container>
    <template>
      <v-data-table
          :headers="headers"
          :items="units"
          :items-per-page="30"
          class="elevation-1"
          @click:row="handleClick"
      >
        <template v-slot:item.Icon="{ item }">
          <v-img
              max-width="60"
              v-bind:src=getPath(item.Icon)
          ></v-img>
        </template>
      </v-data-table>
    </template>
  </v-container>
</template>

<script>
  import axios from 'axios'

  export default {
    name: "Table",
    props: {
      path: String,
    },
    data() {
      return {
        headers: [],
        units: []
      }
    },
    methods: {
      handleClick(item) {
        console.log(item)
      },
      getPath (path) {
        return process.env.VUE_APP_BACKEND_API + 'icon/' + path;
      },
    },
    mounted() {
      axios
        .get(process.env.VUE_APP_BACKEND_API + this.path)
        .then(
          response => {
            this.units = response.data.data
            this.headers = response.data.columns
          }
        )
    }
  }
</script>