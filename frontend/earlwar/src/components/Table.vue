<template>
  <v-container>
    <h2>{{ path }}</h2>
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
              v-bind:src=getIcon(item.Icon)
          ></v-img>
        </template>
      </v-data-table>
    </template>
  </v-container>
</template>

<script>
  import Api from '@/api/api'
  import ApiComponent from "@/components/ApiComponent";

  export default {
    extends: ApiComponent,
    name: "Table",
    data() {
      return {
        headers: [],
        units: [],
      }
    },
    methods: {
      handleClick(item) {
        console.log(item);
      },
      updateData() {
        Api.table({'path': this.path})
          .then(
            response => {
              this.units = response.data.data;
              this.headers = response.data.columns;
            }
          )
      },
      getIcon(path) {
        return Api.iconUrl(path);
      },
    }
  }
</script>