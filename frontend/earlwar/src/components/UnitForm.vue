<template>
  <v-container>
    <h2>{{item.Name}}</h2>
    <validation-observer
        ref="observer"
        v-slot="{ invalid }"
    >
      <v-form v-model="valid"
              @submit.prevent="submit"
      >
        <v-card
            class="mt-10"
            width="1024"
        >
          <v-card-title>Common</v-card-title>
          <v-card-text>
            <three-col-row>
              <template v-slot:1-col>
                <v-text-field
                    v-model="item.Version"
                    label="Version"
                    value="0.1"
                    required
                ></v-text-field>
              </template>
              <template v-slot:2-col>
                <v-text-field
                    v-model="item.Id"
                    label="Id"
                    required
                ></v-text-field>
              </template>
              <template v-slot:3-col>
                <v-text-field
                    v-model="item.Name"
                    label="Name"
                    required
                ></v-text-field>
              </template>
            </three-col-row>
          </v-card-text>
        </v-card>

        <v-card
            class="mt-10"
            width="1024"
        >
          <v-card-title>Unit type</v-card-title>
          <v-card-text>
            <three-col-row>
              <template v-slot:1-col>
                <v-select
                    label="Class"
                    v-model="item.Class"
                    :items="classes"
                ></v-select>
              </template>
              <template v-slot:2-col>
                <v-checkbox
                    v-model="item.IsTower"
                    label="Is tower?"
                ></v-checkbox>
              </template>
            </three-col-row>
          </v-card-text>
        </v-card>

        <v-card
            class="mt-10"
            width="1024"
        >
          <v-card-title>Invasion</v-card-title>
          <v-card-text>
            <v-row>
              <v-col
                  cols="12"
                  md="4"
              >
                <v-checkbox
                    v-model="item.CanJoinInvasion"
                    label="Can Join Invasion?"
                    required
                ></v-checkbox>
              </v-col>

              <v-col
                  cols="12"
                  md="4"
              >
                <validation-provider
                    v-slot="{ errors }"
                    vid="SquadWeight"
                    name="SquadWeight"
                    rules="required|min_value:0.1"
                >
                  <v-text-field
                      v-model="item.SquadWeight"
                      label="SquadWeight"
                      default="1"
                      type="number"
                      step="0.1 "
                      required
                      :error-messages="errors"
                  ></v-text-field>
                </validation-provider>
              </v-col>

              <v-col
                  cols="12"
                  md="4"
              >
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>

        <v-card
            class="mt-10"
            width="1024"
        >
          <v-card-title>Defence</v-card-title>
          <v-card-text>
            0 {{item.MaxHealth}}
            1 {{item.AttackBlockChance}}
            2 {{item.AbilityBlockChance}}
            3 {{item.BlockEfficiency}}
            <three-col-row>
              <template v-slot:1-col>
                <max-h-p
                    required
                    :value="item.MaxHealth"
                ></max-h-p>
              </template>
              <template v-slot:2-col>
                <h-p-regen
                    :value="item.HealthRegenPercent"
                ></h-p-regen>
              </template>
              <template v-slot:3-col>
                <move-speed
                    :value="item.MoveSpeed"
                    :item="item"
                ></move-speed>
              </template>
            </three-col-row>
            <three-col-row>
              <template v-slot:1-col>
                <physical-resistance
                    :value="item.ResistancePhysical"
                ></physical-resistance>
              </template>
              <template v-slot:2-col>
                <magical-resistance
                    :value="item.ResistanceMagic"
                ></magical-resistance>
              </template>
              <template v-slot:3-col>
                <chaotic-resistance
                    :value="item.ResistanceChaos"
                ></chaotic-resistance>
              </template>
            </three-col-row>
            <optional-panel
                :active="!!item.AttackBlockChance || !!item.AbilityBlockChance || !!item.BlockEfficiency">
              <template v-slot:header>Blocks</template>
              <template v-slot:content>
                <three-col-row>
                  <template v-slot:1-col><attack-block :value="item.AttackBlockChance"></attack-block></template>
                  <template v-slot:2-col><ability-block :value="item.AbilityBlockChance"></ability-block></template>
                  <template v-slot:3-col><block-efficiency :value="item.BlockEfficiency"></block-efficiency></template>
                </three-col-row>
              </template>
            </optional-panel>
          </v-card-text>
        </v-card>

        <v-card
            class="mt-10"
            width="1024"
        >
          <v-card-title>Attack</v-card-title>
          <v-card-text>
          </v-card-text>
        </v-card>

        <v-card
            class="mt-10"
            width="1024"
        >
          <v-card-title>Penetration</v-card-title>
          <v-card-text>
          </v-card-text>
        </v-card>

        <v-card
            class="mt-10"
            width="1024"
        >
          <v-card-title>Abilities</v-card-title>
          <v-card-text>
          </v-card-text>
        </v-card>
        <v-btn :disabled="invalid">Submit</v-btn>
        {{item}}
      </v-form>
    </validation-observer>
  </v-container>
</template>

<script>
  import Api from '@/api/api'
  import ApiComponent from "@/components/ApiComponent";

  import ThreeColRow from "@/components/layout/ThreeColRow";
  import OptionalPanel from "@/components/layout/OptionalPanel";

  import MaxHP from "@/components/fields/defence/MaxHP";
  import HPRegen from "@/components/fields/defence/HPRegen";
  import MoveSpeed from "@/components/fields/defence/MoveSpeed";
  import PhysicalResistance from "@/components/fields/defence/PhysicalResistance";
  import MagicalResistance from "@/components/fields/defence/MagicalResistance";
  import ChaoticResistance from "@/components/fields/defence/ChaoticResistance";
  import AttackBlock from "@/components/fields/defence/AttackBlock";
  import AbilityBlock from "@/components/fields/defence/AbilityBlock";
  import BlockEfficiency from "@/components/fields/defence/BlockEfficiency";

  export default {
    components: {
      ThreeColRow,
      OptionalPanel,
      MaxHP,
      HPRegen,
      MoveSpeed,
      PhysicalResistance,
      MagicalResistance,
      ChaoticResistance,
      AttackBlock,
      AbilityBlock,
      BlockEfficiency,
    },
    extends: ApiComponent,
    name: "UnitForm",
    data: function () {
      return {
        item: {
          IsTower: false,
        },
        classes: ["Defender", "Warrior", "Assassin", "Archer", "Mage", "Siege", "Support", "Healer", "Summoner"]
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