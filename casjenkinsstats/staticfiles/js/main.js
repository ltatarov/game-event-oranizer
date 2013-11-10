$(document).ready(function(){

    // add guest
    $("body").on("click", "input[name^='newGuestButton_']", function(){
        // get params out of object name
        var tableId = parseInt($(this).attr('name').split('_')[1]);
        var guestName = $("#newGuestName_" + tableId).val();
        if (guestName == ""){
            alert("you must have a name to sign up");
            return
        }

        var guest = {
            name: guestName
        };
        $.get("/guest/add",
            {
                tableId: tableId, guest: $.param(guest)
            },
            function(data){

//                data = $.parseJSON(data);
                var guestId = data['guestId'];

                // prepare new guest element
                var newGuest = createNewGuestElement(guestId, guestName);
                $("#guestsList_" + tableId).append(newGuest);


                // check if max guests exceeded
                var table = $("#table_" + tableId);
                var guests = table.find("li.guest");
                var maxGuests = table.find("#maxGuests").attr("maxGuests");
                var addGuestDiv = table.find("#newGuest_" + tableId);
                if (guests.length >= maxGuests) {
                    addGuestDiv.addClass("display-none");
                }
                table.find("#newGuestName_" + tableId).val("");
            }
        );
    });

    function createNewGuestElement(guestId, guestName, isAdmin){
        var newGuest = $("#guest_template").clone();
        newGuest.attr("id", "guest_" + guestId);

        var guestNameText = newGuest.find("#guestName");
        guestNameText.text(guestName);
        if (location.pathname.indexOf("admin") !== -1){
            var newGuestRemove = newGuest.find(".remove");
            newGuestRemove.attr("name", "deleteGuestButton_" + guestId);
        }
        newGuest.removeClass("display-none");

        return newGuest;
    }

});


