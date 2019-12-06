
var user = load_user_data();
create_stats_card();
create_card_deck();
create_user_networth_chart(user);

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

function load_user_data(){
    var r = new XMLHttpRequest();
    r.open("GET", "http://student04.cse.nd.edu:51075/users/" + 1, false);
    r.onload = function (e) {
        console.log(r.responseText);
    }
    r.onerror = function (e) {
        console.error(r.statusText);
    }
    r.send(null);    
    data = JSON.parse(r.responseText);
    return data 
}

function convertToUSD (amount, showSign) {
    var USD_string = "";
    if (amount < 0) {
        if (showSign) USD_string = "- ";
        amount *= -1;
        USD_string += "$" + amount.toFixed(2).toString();
    } else {
        if (showSign) USD_string = "+ ";
        USD_string += "$" + amount.toFixed(2).toString();
    }
    return USD_string;
}

function create_stats_card () {
    // Get Networth
    var net_worth = get_portfolio_amount();
    var networth_text = document.getElementById('networth_text');
    networth_text.innerHTML = "$" + net_worth.toFixed(2).toString();
    networth_text.innerHTML = convertToUSD(net_worth, false);

    // Get Net Change
    var net_change = get_portfolio_change();
    var growth_text = document.getElementById('growth_text');
    growth_text.innerHTML = convertToUSD(net_change, true);
}
    

function create_card_deck () {
    var data = user;
    stocks = data["stocks"]; //stocks of the user 
    var id = 0
    //for (i = 0; i < Object.keys(stocks).length; i++) {for( Enumeration e = stocks.keys(); e.hasMoreElements()){
    for( x in stocks){
        var stock = JSON.parse(load_stock(x)); //load the info on the stock 
        var price = stock[x]["regularMarketPrice"]; //get out the market price 
        var change = stock[x]["regularMarketChange"]; //get out the market change
        change = change.toFixed(2);
        var num = stocks[x];
        var card = new Card(id, x, price, change, num);
        
        document.getElementById("users-card-deck").appendChild(document.getElementById("card_" + id));
        id = id + 1;
    }
}

// @func : get_portfolio_amount
// @desc : N/A
function get_portfolio_amount () {
    var data = user;
    var stocks = data["stocks"];
    var sum = 0;
    for (symbol in stocks) {
        var stock = JSON.parse(load_stock(symbol)); //load the info on the stock 
        var count = stocks[symbol]; //multiplier
        var price = stock[symbol]["regularMarketPrice"];
        sum += count * price;
    }
    return sum;
}

function get_portfolio_change () {
    var data = user;
    var stocks = data["stocks"];
    var sum = 0;
    for (symbol in stocks) {
        var stock = JSON.parse(load_stock(symbol)); //load the info on the stock 
        var count = stocks[symbol]; //multiplier
        var price = stock[symbol]["regularMarketChange"];
        sum += count * price;
    }
    return sum;
}