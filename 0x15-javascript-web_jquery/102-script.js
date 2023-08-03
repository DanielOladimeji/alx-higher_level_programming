'use strict';

document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').click(function () {
    const url = 'hhttps://www.fourtonfish.com/hellosalut/hello/';
    const language = $('INPUT#language_code').val();
    $.get(url + language, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
