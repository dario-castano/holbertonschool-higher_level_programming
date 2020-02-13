$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, _) {
    $('div#hello').append(data.hello);
  });
});
