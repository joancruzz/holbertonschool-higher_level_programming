// Script that fetches and lists all movies title by this URL
$.ajax({
  url: 'https://swapi.co/api/films/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (response) {
    for (let i = 0; i < response.results.length; i++) {
      $('#list_movies').append('<li>' + response.results[i].title + '</li>');
    }
  }
});
