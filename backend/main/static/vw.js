import Vue from './modules/vue.esm.browser.js';
import VueFormGenerator from './modules/vfg.js';
import ModuleLibrary from './modules/vfg-field-array.esm.js';

Vue.use(VueFormGenerator);
Vue.use(ModuleLibrary);

export default {
    el: "#app",
    components: {
        "vue-form-generator": VueFormGenerator.component
    },
    data() {
        return {
            model: {},
            schema: {
                groups: [
                    {
                        legend: "User Details",
                        fields: [
                            {
                                type: "input",
                                inputType: "text",
                                label: "Name",
                                model: "name"
                            },
                            {
                                type: "input",
                                inputType: "number",
                                id: "current_age",
                                label: "Age",
                                model: "age"
                            }
                        ]
                    },
                    {
                        legend: "Other details",
                        fields: [
                            {
                                type: "input",
                                inputType: "text",
                                label: "Name",
                                model: "name"
                            },
                            {
                                type: "select",
                                label: "Language",
                                required: true,
                                values: [
                                    {name: "Marc Marquez", id: "93", group: "MotoGP"},
                                    {name: "Valentino Rossi", id: "46", group: "MotoGP"},
                                    {name: "Lewis Hamilton", id: "44", group: "Formula 1"},
                                    {name: "Sebastian Vettel", id: "5", group: "Formula 1"}
                                ],
                            }
                        ]
                    }
                ]
            },

            formOptions: {
                validateAfterLoad: true,
                validateAfterChanged: true
            }
        };
    }
};