$(document).ready(() => {
    $("input#btn_translate").click(() => {
        let langCode = $("input#language_code").val();
        $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${langCode}`,
            (data) => {
                $("div#hello").text(data.hello);
            }
        );
    });
});