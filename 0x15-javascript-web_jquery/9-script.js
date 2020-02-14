// Script that fetches from URL and displays the
// value from that fetch in the HTML’s tag DIV#hello.
$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  type: 'GET',
  dataType: 'json',
  success: function (response) {
    for (let i = 0; i < response.hello.length; i++) {
      $('#hello').append(response.hello[i]);
    }
  }
});
