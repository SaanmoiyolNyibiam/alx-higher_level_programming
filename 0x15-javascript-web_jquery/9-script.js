$(document).ready(function() {
    $.ajax({
        type: 'GET',
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        success: function(data) {
            $("div#hello").append(data.hello);
        }
    });
});