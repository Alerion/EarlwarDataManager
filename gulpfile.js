const { series, src, dest } = require('gulp');

// Task 1: copy bootstap's assets to /_vendor/
function tree() {
  const files = [
    'node_modules/bstreeview/src/css/bstreeview.css',
    'node_modules/bstreeview/src/js/bstreeview.js'
  ]
  return src(files).pipe(dest('_vendor'))
}

exports.default = series(tree)