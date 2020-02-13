$(document).ready(function () {
  $.get('https://swapi.co/api/films?format=json', function (data, _) {
    for (let x of data.results) {
      $('ul#list_movies').append('<li>' + x.title + '</li>');
    }
  });
});
