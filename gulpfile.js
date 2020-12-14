const {src, series, dest} = require('gulp'),
   uglify = require('gulp-terser'),
   concat = require('gulp-concat');

function js() {
  const files = [
    'node_modules/jquery/dist/jquery.min.js',
    'node_modules/popper.js/dist/umd/popper.min.js',
    'node_modules/bootstrap/dist/js/bootstrap.min.js',
    'node_modules/bootstrap-table/dist/bootstrap-table.min.js',
    'node_modules/bstreeview/dist/js/bstreeview.min.js',
    'node_modules/select2/dist/js/select2.min.js',
    'main/static/js/*.js',
  ]
  return src(files)
      .pipe(uglify())
      .pipe(concat('app.js'))
      .pipe(dest('main/static'))
}

function css() {
  const files = [
    'node_modules/bootstrap/dist/css/bootstrap.min.css',
    'node_modules/bootstrap-table/dist/bootstrap-table.min.css',
    'node_modules/bstreeview/dist/css/bstreeview.min.css',
    'node_modules/select2/dist/css/select2.min.css',
  ]
  return src(files)
      .pipe(concat('app.css'))
      .pipe(dest('main/static'))
}

exports.default = series(js, css)
