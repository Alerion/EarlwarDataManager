$('document').ready(function() {

    // Get value from either a json string or url pointing to a json file
    function process(value) {
        var isjson=true;
        var result;

        try {
          result = JSON.parse(value);
        } catch(e) {
          isjson=false;
        }

        if (isjson) {
          return result;
        } else {
          return $.getJSON(value)
            .then(function (response) {
                return response;
            });
        }
    }


    $('.editor_holder').each(function() {
        // Get the DOM Element
        let element = $(this).get(0);

        let options_text = $(this).attr('options')
        let schema_text = $(this).attr('schema')

        let options = process(options_text);

        let name = $(this).attr('name');
        let hidden_identifier = 'input[name=' + name + ']';
        let initial = $(hidden_identifier).val();

        // Check if editor is within form
        let form = $(this).closest('form')

        //Wait for any ajax requests to complete
        $.when(options).done(function(optionsresult) {
            optionsresult.form_name_root = name;

            // Pass initial value though to editor
            if (initial) {
                optionsresult.startval = JSON.parse(initial);
            }

            optionsresult.schema = {
                $ref: schema_text,
                format: "grid"
            };
            // Add a resolver function to the beginning of the resolver list
            let editor = new JSONEditor(element, optionsresult);

            if (form) {
                $(form).submit(function() {
                    // Set the hidden field value to the editors value
                    $(hidden_identifier).val(JSON.stringify(editor.getValue()));
                    // Disable the editor so it's values wont be submitted
                    editor.disable();
                })
            }
        })
    });
})
