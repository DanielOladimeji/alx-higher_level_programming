'use strict';

document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').click(function () {
    const url = 'https://www.fourtonfish.com/hellosalut/hello/';
    const language = $('INPUT#language_code').val();
    $.get(url + language, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
  $('INPUT#language_code').on('keypress', function (event) {
    if (event.which === 13) {
      const url = 'https://www.fourtonfish.com/hellosalut/hello/';
      const language = $('INPUT#language_code').val();
      $.get(url + language, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});
