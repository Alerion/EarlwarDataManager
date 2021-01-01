<script>
  export default {
    name: 'Field',
    props: {
      value: Number,
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
      type: function (val) {
        return Number(val)
      }
    },
    computed: {
      internalValue: {
        get() {
          return this.lazyValue;
        },
        async set(val) {
          this.lazyValue = val;
          const result = await this.$refs.validation.validate(val);
          console.log(result.valid)
          if (result.valid) {
            this.$emit('input', this.type(val));
          }
        },
      },
    },
  };
</script>