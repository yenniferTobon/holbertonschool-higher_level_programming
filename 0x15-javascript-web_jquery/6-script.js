// updates the text tag HEADER to “New Header!!!” when the user clicks on DIV#update_header

$('DIV#update_header').click(function () {
  $('header').text('New Header!!!');
});
