import Vue from 'vue';

import { ValidationObserver, ValidationProvider, extend } from 'vee-validate';
import { required, max, min_value, max_value, excluded } from 'vee-validate/dist/rules';


Vue.component('validation-observer', ValidationObserver);
Vue.component('validation-provider', ValidationProvider);

// Try to keep messages equal to REST API error messages
extend('min_value', min_value)
extend('max_value', max_value)
extend('required', {
    ...required,
    message: 'this field is required',
});

extend('max', {
    ...max,
    message: 'ensure this value has at most {length} characters',
});

extend('weight', {
    validate(value) {
        const weight = Number(value);
        return !Number.isNaN(weight) && weight > 0;
    },
    message: 'value should be positive float',
});

extend('excluded', {
    ...excluded,
    validate(value, params) {
        console.log(params);
        return !params.includes(value);
    },
    message: 'impossible value',
})
