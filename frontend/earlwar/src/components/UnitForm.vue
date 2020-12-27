<template>
  <v-container>
    <h2>{{item.Name}}</h2>
    <v-form v-model="valid">
      <v-card
          elevation="2"
      >
        <v-card-title>Common</v-card-title>
        <v-container>
          <v-row>
            <v-col
                cols="12"
                md="4"
            >
              <v-text-field
                  v-model="item.Version"
                  label="Version"
                  value="0.1"
                  required
              ></v-text-field>
            </v-col>

            <v-col
                cols="12"
                md="4"
            >
              <v-text-field
                  v-model="item.Id"
                  label="Id"
                  required
              ></v-text-field>
            </v-col>

            <v-col
                cols="12"
                md="4"
            >
              <v-text-field
                  v-model="item.Name"
                  label="Name"
                  required
              ></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-card>
      {{item}}
    </v-form>
  </v-container>
</template>

<script>
  import Api from '@/api/api'
  import ApiComponent from "@/components/ApiComponent";

  export default {
    extends: ApiComponent,
    name: "UnitForm",
    data: function () {
      return {
        item: {}
      }
    },
    methods: {
      updateData() {
        Api.item({'path': this.path})
          .then(
            response => {
              this.item = response.data;
            }
          )
      },
    }
  }

</script>