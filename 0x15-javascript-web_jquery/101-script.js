$(document).ready(() => {
    //adds a new element to the list
    $("div#add_item").click(() => {
        $("ul.my_list").append("<li>item</li>");
    });

    //removes the last item from the list
    $("div#remove_item").click(() => {
        $("ul.my_list li:last-child").remove();
    });

    //removes all elements of the list
    $("div#clear_list").click(() => {
        $("ul.my_list").empty();
    });
})