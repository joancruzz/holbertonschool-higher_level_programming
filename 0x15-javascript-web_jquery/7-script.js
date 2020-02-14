// Script that fetches and replaces the name URL
$.ajax({
  url: 'https://swapi.co/api/people/5/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (response) {
    $('#character').text(response.name);
  }
});
