
$('#search_modal').on('show.bs.modal', function (event) {
    // Load User Data
    var user_data = load_user_data();
    var button = $(event.relatedTarget)
    var stock = button.data('whatever')
    var modal = $(this)
    modal.find('.modal-title').text('Purchase Stock For ' + stock)
    modal.find('.modal-body input').val('0')

    document.getElementById("submit_button").onmouseup = function () {
        var amount = parseInt(document.getElementById("amount").value);
            if (stock in user_data['stocks']) {
                user_data['stocks'][stock] = parseInt(user_data['stocks'][stock]) + amount;
            } else {
                user_data['stocks'][stock] = amount;
            }
        
            put_user_data(user_data);

            //create_card_deck();
            window.location.reload();
    }
    
  });




  
