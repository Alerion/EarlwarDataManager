<script>
  export default {
    name: 'BaseField',
    props: {
      value: null,
      item: {},
      required: {
        type: Boolean,
        default: false,
      },
    },

    data() {
      return {
        lazyValue: this.value,
      };
    },

    watch: {
      value(val) {
        this.lazyValue = val;
      },
    },
    methods: {
      convertType(val) {
        return String(val)
      },
      disableCondition() {
        return false
      },
      setNull() {
        this.$emit('input', null);
      }
    },
    computed: {
      isDisabled: function () {
        const condition = this.disableCondition();
        if (condition) {
          this.setNull();
        }
        return condition;
      },
      internalValue: {
        get() {
          return this.lazyValue;
        },
        async set(val) {
          this.lazyValue = val;
          const result = await this.$refs.validation.validate(val);
          if (result.valid) {
            this.$emit('input', this.convertType(val));
          }
        },
      },
    },
  };
</script>