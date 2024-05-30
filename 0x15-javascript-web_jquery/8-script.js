$(document).ready(function() {
    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        success: function(data) {
            data.results.forEach(function(film) {
                $("ul#list_movies").append(`<li>${film.title}</li>`)
            })
        }
    })
})