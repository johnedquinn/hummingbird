

// Update both card decks
update_card_deck(0, "gainers");
update_card_deck(1, "losers");

// @func  : load_top_movers
// @desc  : grab top movers
function load_top_movers () {
    var r = new XMLHttpRequest();
    r.open("GET", "http://student04.cse.nd.edu:51075/movers/", false);
    r.onload = function (e) {
        console.log(r.responseText);
    }
    r.onerror = function (e) {
        console.error(r.statusText);
    }
    r.send(null);
    return r.responseText;
}

// @func  : load_stock
// @desc  : grab specific stock
function load_stock (symbol) {
    var r = new XMLHttpRequest();
    r.open("GET", "http://student04.cse.nd.edu:51075/quotes/" + symbol, false);
    r.onload = function (e) {
        console.log(r.responseText);
    }
    r.onerror = function (e) {
        console.error(r.statusText);
    }
    r.send(null);
    return r.responseText;
}

// @func  : get_mover_info
// @desc  : gets the movers quotes
function get_mover_info (id) {
    var top_movers = JSON.parse(load_top_movers());
    var target = top_movers["movers"][id]["quotes"];
    return target;
}

// @func  : update_card_deck
// @desc  : places three cards onto a card deck
// @param : index = 0 => gainers; 1 => losers; 2 => active
// @param : name  = name of card deck
function update_card_deck (index, name) {

    // Get all movers
    var movers = get_mover_info(index);

    // Grab the top 3 losers/gainers
    // Use index * 3 to make sure IDs are not same
    for (i = index * 3; i < (index * 3 + 3); i++) {
        // Parse Data
        var quote = movers[i];
        var stock = JSON.parse(load_stock(quote["symbol"]));
        var title = quote["symbol"];
        var subtitle = stock[title]["longName"];
        var body = stock[title]["regularMarketChangePercent"].toFixed(2).toString() + "%";

        // Create Card
        var card = new Card(i, title, subtitle, body);
        document.getElementById(name + "-card-deck").appendChild(document.getElementById("card_" + i));
    }
}