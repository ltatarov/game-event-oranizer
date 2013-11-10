$(document).ready(function(){

    // delete guest
    $("body").on("click", "span[name^='deleteGuestButton_']", function(){
        // get params out of object name
        var guestId = parseInt($(this).attr('name').split('_')[1]);
        var tableId = parseInt($(this).attr('name').split('_')[2]);

        $.get("/guest/delete",
            {
                guestId: guestId, tableId: tableId
            },
            function(){
                // add guest object
                var table = $("#table_" + tableId);

                var guest = table.find("#guest_" + guestId);
                guest.remove();

                // check if max guests exceeded
                var guests = table.find("li.guest");
                var maxGuests = table.find("#maxGuests").attr("maxGuests");
                if (guests.length < maxGuests) {
                    var newGuestDiv = table.find("#newGuest_" + tableId);
                    newGuestDiv.removeClass("display-none");
                }
            }
        );
    });

    // delete table
    $("body").on("click", "div[name^='deleteTableButton_']", function(){
        // get params out of object name
        var tableId = parseInt($(this).attr('name').split('_')[1]);

        $.get("/table/delete",
            {
                tableId: tableId
            },
            function(){
                // add guest object
                var table = $("#table_" + tableId);
                table.remove();
            }
        );
    });
});


