/// A JQuery API to get title os star wars movies from a url
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
