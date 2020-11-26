function linkFormatter(value, row) {
    if (row.Path !== undefined) {
        return "<a href='/edit/" + row.Path + "/form'>Edit</a> <a href='/delete/" + row.Path + "'>Del</a>"
    }
    return ""
}

function buttons() {
    return {
        btnAdd: {
            text: 'Add new item',
            icon: 'fa-plus',
            event: function () {
                $('#addModal').modal()
            },
            attributes: {
              title: 'Add a new item'
            }
        }
    }
}