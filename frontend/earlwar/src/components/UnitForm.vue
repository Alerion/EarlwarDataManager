<template>
  <v-container>
    <h2>{{item.Name}}</h2>
    <validation-observer
        ref="observer"
        v-slot="{ invalid }"
    >
      <v-form
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
            <three-col-row>
              <template v-slot:1-col>
                <v-checkbox
                    v-model="item.CanJoinInvasion"
                    label="Can Join Invasion?"
                    required
                ></v-checkbox>
              </template>
              <template v-slot:2-col>
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
              </template>
            </three-col-row>
          </v-card-text>
        </v-card>

        <v-card
            class="mt-10"
            width="1024"
        >
          <v-card-title>Defence</v-card-title>
          <v-card-text>
            <three-col-row>
              <template v-slot:1-col>
                <max-h-p
                    required
                    v-model="item.MaxHealth"
                ></max-h-p>
              </template>
              <template v-slot:2-col>
                <h-p-regen
                    v-model="item.HealthRegenPercent"
                ></h-p-regen>
              </template>
              <template v-slot:3-col>
                <move-speed
                    v-model="item.MoveSpeed"
                    :item="item"
                ></move-speed>
              </template>
            </three-col-row>
            <three-col-row>
              <template v-slot:1-col>
                <physical-resistance
                    v-model="item.ResistancePhysical"
                ></physical-resistance>
              </template>
              <template v-slot:2-col>
                <magical-resistance
                    v-model="item.ResistanceMagic"
                ></magical-resistance>
              </template>
              <template v-slot:3-col>
                <chaotic-resistance
                    v-model="item.ResistanceChaos"
                ></chaotic-resistance>
              </template>
            </three-col-row>
            <optional-panel
                :active="!!item.AttackBlockChance || !!item.AbilityBlockChance || !!item.BlockEfficiency">
              <template v-slot:header>Blocks</template>
              <template v-slot:content>
                <three-col-row>
                  <template v-slot:1-col>
                    <attack-block v-model="item.AttackBlockChance"></attack-block>
                  </template>
                  <template v-slot:2-col>
                    <ability-block v-model="item.AbilityBlockChance"></ability-block>
                  </template>
                  <template v-slot:3-col>
                    <block-efficiency v-model="item.BlockEfficiency"></block-efficiency>
                  </template>
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
            <three-col-row>
              <template v-slot:1-col>
                <attack-type
                    v-model="item.AttackType"
                    :item="item"
                ></attack-type>
              </template>
              <template v-slot:2-col>
                <attack-damage-type
                    v-model="item.AttackDamageType"
                    :item="item"
                ></attack-damage-type>
              </template>
              <template v-slot:3-col>
                <attack-range
                    v-model="item.AttackRange"
                    :item="item"
                ></attack-range>
              </template>
            </three-col-row>
            <three-col-row>
              <template v-slot:1-col>
                <attack-damage v-model="item" :item="item"></attack-damage>
              </template>
              <template v-slot:2-col>
              </template>
              <template v-slot:3-col>
              </template>
            </three-col-row>
            <optional-panel
                :active="!!item.CritChance || !!item.CritMultiplier">
              <template v-slot:header>Has crits</template>
              <template v-slot:content>
                <three-col-row>
                  <template v-slot:1-col>
                    <crit-chance v-model="item.CritChance"></crit-chance>
                  </template>
                  <template v-slot:2-col>
                    <crit-multiplier v-model="item.CritMultiplier"></crit-multiplier>
                  </template>
                </three-col-row>
              </template>
            </optional-panel>
            <optional-panel
                :active="hasAOE"
                class="mt-5"
            >
              <template v-slot:header>AOE</template>
              <template v-slot:content>
                <three-col-row>
                  <template v-slot:1-col>
                    <a-o-e-radius v-model="item.AttackAOE.Radius"></a-o-e-radius>
                  </template>
                  <template v-slot:2-col>
                    <a-o-e-damage-type v-model="item.AttackAOE.DamageType"></a-o-e-damage-type>
                  </template>
                  <template v-slot:3-col>
                    <a-o-e-damage v-model="item.AttackAOE" :item="item.AttackAOE"></a-o-e-damage>
                  </template>
                </three-col-row>
              </template>
            </optional-panel>
          </v-card-text>
        </v-card>

        <v-card
            class="mt-10"
            width="1024"
        >
          <v-card-title>Penetration</v-card-title>
          <v-card-text>
            <three-col-row>
              <template v-slot:1-col></template>
              <template v-slot:2-col></template>
              <template v-slot:3-col></template>
            </three-col-row>
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
  import AttackBlock from "@/components/fields/defence/blocks/AttackBlock";
  import AbilityBlock from "@/components/fields/defence/blocks/AbilityBlock";
  import BlockEfficiency from "@/components/fields/defence/blocks/BlockEfficiency";
  import AttackType from "@/components/fields/attack/AttackType";
  import AttackDamageType from "@/components/fields/attack/AttackDamageType";
  import AttackRange from "@/components/fields/attack/AttackRange";
  import AttackDamage from "@/components/fields/attack/AttackDamage";
  import CritChance from "@/components/fields/attack/crits/CritChance";
  import CritMultiplier from "@/components/fields/attack/crits/CritMultiplier";
  import AOEDamage from "@/components/fields/attack/aoe/AOEDamage";
  import AOERadius from "@/components/fields/attack/aoe/AOERadius";
  import AOEDamageType from "@/components/fields/attack/aoe/AOEDamageType";

  export default {
    components: {
      AOEDamageType,
      AOERadius,
      AOEDamage,
      CritMultiplier,
      CritChance,
      AttackDamage,
      AttackRange,
      AttackDamageType,
      AttackType,
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
      const data = this.getDefaultData();
      return {
        item: data,
        classes: ["Defender", "Warrior", "Assassin", "Archer", "Mage", "Siege", "Support", "Healer", "Summoner"]
      }
    },
    watch: {
      item(data) {
        this.updateDataFromItem(this.item, data);
      }
    },
    computed: {
      hasAOE() {
        return Object.keys(this.item.AttackAOE).length !== 0 || this.item.AttackAOE.constructor !== Object
      }
    },
    methods: {
      updateData() {
        Api.item({'path': this.path})
          .then(
            response => {
              this.updateDataFromItem(this.item, response.data);
            }
          )
      },
      updateDataFromItem(item, data) {
        if (data) {
          const itemCopy = JSON.parse(JSON.stringify(data));
          Object.keys(item).forEach((key) => {
            item[key] = typeof itemCopy[key] !== "undefined" ? itemCopy[key] : item[key];
          });
        }
      },
      getDefaultData() {
        return {
          Version: null,
          Id: null,
          Name: null,
          Class: null,
          Description: null,
          CanJoinInvasion: true,
          MaxHealth: 0,
          ResistancePhysical: 0,
          ResistanceMagic: 0,
          ResistanceChaos: 0,
          AttackType: null,
          AttackDamageType: null,
          AttackRange: null,
          AttackBlockChance: null,
          AbilityBlockChance: null,
          BlockEfficiency: null,
          DamageMin: null,
          DamageMax: null,
          CritChance: null,
          CritMultiplier: null,
          AttackSpeed: null,
          AttackAOE: {},
          Abilities: [],
          Upgrades: [],
        };
      },
    }
  }

</script>