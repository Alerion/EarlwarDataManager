$('document').ready(function() {

    JSONEditor.defaults.editors.leveled = class leveled extends JSONEditor.defaults.editors.string {
          getValue () {
              const value = super.getValue()
              return value !== "" ? JSON.parse(value) : value
          }
    }

    JSONEditor.defaults.resolvers.unshift(
        schema => schema.type === "array" && schema.format === "leveled" ? "leveled" : ""
    )
})