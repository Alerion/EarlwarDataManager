function linkFormatter(value, row) {
    if (row.Path !== undefined) {
        var edit = document.createElement('a', {
            href: '/edit/' + row.Path + '/form'
        })
        return "<a href='/edit/" + row.Path + "/form'>Edit</a>" +
            " <a href='/delete/" + row.Path + "'>Del</a>" +
            " <a href='#' data-toggle='modal' >"
    }
    return ""
}

function buttons() {
    return {
        btnAdd: {
            text: 'Add new file',
            icon: 'fa-plus',
            attributes: {
                'title': 'Add a new file',
                'data-toggle': 'modal',
                'data-target': '#addModal',
                'data-action': '/add/file'
            }
        },
        btnAddFolder: {
            text: 'Add new folder',
            icon: 'fa-folder-plus',
            attributes: {
                'title': 'Add a new folder',
                'data-toggle': 'modal',
                'data-target': '#addModal',
                'data-action': '/add/folder'
            }
        }
    }
}

$(function () {
    $('#addModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget)
        var modal = $(this)
        modal.find('form').attr('action', button.data('action'))
        modal.find('#name').attr('placeholder', button.data('placeholder'))
        modal.find('h5').text(button.attr('title'))
    })
})