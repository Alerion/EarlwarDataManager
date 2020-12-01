function button(href, content, attributes) {
    attributes = attributes ? attributes : {}
    const dataAttrs = Object.keys(attributes).map(function(key) {
        return key + '="' + attributes[key] + '"'
    }).join(' ');
    return '<a class="btn" href="' + href + '" ' + dataAttrs + '>' + content + '</a>'
}

function icon(customClass) {
    return '<i class="fa ' + customClass + '"></i>'
}

function linkFormatter(value, row) {
    if (!row || !row.Path) {
        return
    }
    return button('/edit/' + row.Path + '/form', icon('fa-pen')) +
        button('/delete/' + row.Path + '/form', icon('fa-trash')) +
        button('#', icon('fa-i-cursor'), {
            'data-toggle': 'modal',
            'data-target': '#addModal',
            'data-action': '/rename/file',
            'title': 'Rename',
        })
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