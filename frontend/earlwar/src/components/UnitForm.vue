<template>
  <v-container>
    <h2>{{data.Name}}</h2>
    <validation-observer
        ref="observer"
        v-slot="{ handleSubmit }"
    >
      <v-form
          @submit.prevent="handleSubmit(onSubmit)"
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
                    v-model="data.Version"
                    label="Version"
                    value="0.1"
                    required
                ></v-text-field>
              </template>
              <template v-slot:2-col>
                <v-text-field
                    v-model="data.Id"
                    label="Id"
                    required
                ></v-text-field>
              </template>
              <template v-slot:3-col>
                <v-text-field
                    v-model="data.Name"
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
                    v-model="data.Class"
                    :items="classes"
                ></v-select>
              </template>
              <template v-slot:2-col>
                <v-checkbox
                    v-model="data.IsTower"
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
                    v-model="data.CanJoinInvasion"
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
                      v-model="data.SquadWeight"
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
                    v-model="data.MaxHealth"
                ></max-h-p>
              </template>
              <template v-slot:2-col>
                <h-p-regen
                    v-model="data.HealthRegenPercent"
                ></h-p-regen>
              </template>
              <template v-slot:3-col>
                <move-speed
                    v-model="data.MoveSpeed"
                    :item="data"
                ></move-speed>
              </template>
            </three-col-row>
            <three-col-row>
              <template v-slot:1-col>
                <physical-resistance
                    v-model="data.ResistancePhysical"
                ></physical-resistance>
              </template>
              <template v-slot:2-col>
                <magical-resistance
                    v-model="data.ResistanceMagic"
                ></magical-resistance>
              </template>
              <template v-slot:3-col>
                <chaotic-resistance
                    v-model="data.ResistanceChaos"
                ></chaotic-resistance>
              </template>
            </three-col-row>
            <optional-panel
                :active="!!data.AttackBlockChance || !!data.AbilityBlockChance || !!data.BlockEfficiency">
              <template v-slot:header>Blocks</template>
              <template v-slot:content>
                <three-col-row>
                  <template v-slot:1-col>
                    <attack-block v-model="data.AttackBlockChance"></attack-block>
                  </template>
                  <template v-slot:2-col>
                    <ability-block v-model="data.AbilityBlockChance"></ability-block>
                  </template>
                  <template v-slot:3-col>
                    <block-efficiency v-model="data.BlockEfficiency"></block-efficiency>
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
                    v-model="data.AttackType"
                    :item="data"
                ></attack-type>
              </template>
              <template v-slot:2-col>
                <attack-damage-type
                    v-model="data.AttackDamageType"
                    :item="data"
                ></attack-damage-type>
              </template>
              <template v-slot:3-col>
                <attack-range
                    v-model="data.AttackRange"
                    :item="data"
                ></attack-range>
              </template>
            </three-col-row>
            <three-col-row>
              <template v-slot:1-col>
                <attack-damage v-model="data" :item="data"></attack-damage>
              </template>
              <template v-slot:2-col>
              </template>
              <template v-slot:3-col>
              </template>
            </three-col-row>
            <optional-panel
                :active="!!data.CritChance || !!data.CritMultiplier">
              <template v-slot:header>Has crits</template>
              <template v-slot:content>
                <three-col-row>
                  <template v-slot:1-col>
                    <crit-chance v-model="data.CritChance"></crit-chance>
                  </template>
                  <template v-slot:2-col>
                    <crit-multiplier v-model="data.CritMultiplier"></crit-multiplier>
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
                    <a-o-e-radius v-model="data.AttackAOE.Radius"></a-o-e-radius>
                  </template>
                  <template v-slot:2-col>
                    <a-o-e-damage-type v-model="data.AttackAOE.DamageType"></a-o-e-damage-type>
                  </template>
                  <template v-slot:3-col>
                    <a-o-e-damage v-model="data.AttackAOE" :item="data.AttackAOE"></a-o-e-damage>
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
              <template v-slot:1-col>
                <penetration-physical :item="data"></penetration-physical>
              </template>
              <template v-slot:2-col>
                <penetration-magic :item="data"></penetration-magic>
              </template>
              <template v-slot:3-col>
                <penetration-chaos :item="data"></penetration-chaos>
              </template>
            </three-col-row>
          </v-card-text>
        </v-card>
        <ability-panel :abilities="data.Abilities"></ability-panel>
        <v-btn class="mt-5">Submit</v-btn>
      </v-form>
    </validation-observer>
  </v-container>
</template>

<script>
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
  import PenetrationPhysical from "@/components/fields/penetration/PenetrationPhysical";
  import PenetrationMagic from "@/components/fields/penetration/PenetrationMagic";
  import PenetrationChaos from "@/components/fields/penetration/PenetrationChaos";
  import AbilityPanel from "@/components/fields/abilities/AbilityPanel";

  export default {
    components: {
      AbilityPanel,
      PenetrationChaos,
      PenetrationMagic,
      PenetrationPhysical,
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
    props: {
      item: Object,
    },
    data() {
      const data = this.getDefaultData();
      return {
        data: data,
        classes: ["Defender", "Warrior", "Assassin", "Archer", "Mage", "Siege", "Support", "Healer", "Summoner"]
      }
    },
    watch: {
      item(item) {
        this.updateDataFromItem(item, this.data);
      },
    },
    computed: {
      hasAOE() {
        return Object.keys(this.data.AttackAOE).length !== 0 || this.data.AttackAOE.constructor !== Object
      }
    },
    methods: {
      updateDataFromItem(item, data) {
        if (item) {
          const itemCopy = JSON.parse(JSON.stringify(item));
          Object.keys(data).forEach((key) => {
            if (typeof itemCopy[key] === "undefined" && this.getDefaultData()[key]) {
              data[key] = this.getDefaultData()[key];
            } else {
              data[key] = itemCopy[key];
            }
          });
        }
      },
      onSubmit() {
            const data = {
                ...(this.item || {}), // keep fields that are not updated with form
                ...this.data,
            };
            this.doSave(data, this.onSuccess, this.onError);
        },

        onSuccess(item) {
            this.setSuccess(`${this.modelName} saved`);
            this.data = {
                ...(this.item || {}),
                ...this.data,
                ...item, // add fields returned from server
            };
            this.$emit('success', JSON.parse(JSON.stringify(this.data)));
        },

        onError(errors) {
            this.$refs.observer.setErrors(errors);
        },

        doSave(data, onSuccess, onError) {
            // not implemented
        },
      getDefaultData() {
        return {
          Version: null,
          Id: null,
          Name: null,
          Class: null,
          Description: null,
          IsTower: null,
          CanJoinInvasion: null,
          MaxHealth: null,
          ResistancePhysical: null,
          ResistanceMagic: null,
          ResistanceChaos: null,
          AttackType: null,
          AttackDamageType: null,
          AttackRange: null,
          AttackBlockChance: null,
          AbilityBlockChance: null,
          BlockEfficiency: null,
          AttackLifeGainOnHit: null,
          PenetrationPhysical: null,
          PenetrationPhysicalPercent: null,
          PenetrationMagic: null,
          PenetrationMagicPercent: null,
          PenetrationChaos: null,
          PenetrationChaosPercent: null,
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