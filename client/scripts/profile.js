create_card_deck();

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

function create_card_deck () {
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
    console.log(data)
    stocks = data["stocks"]; //stocks of the user 
    console.log(stocks)
    console.log(Object.keys(stocks).length)
    var id = 0
    //for (i = 0; i < Object.keys(stocks).length; i++) {for( Enumeration e = stocks.keys(); e.hasMoreElements()){
    for( x in stocks){
        console.log("stock #")
        console.log(x);
        //var symbol = stocks[x]; //trying to get the symbol of the specific stock
        var stock = JSON.parse(load_stock(x)); //load the info on the stock 
        console.log(stock);
        var price = stock[x]["regularMarketPrice"]; //get out the market price 
        console.log(price);
        var change = stock[x]["regularMarketChange"]; //get out the market change 
        var card = new Card(id, x, price, change);
        document.getElementById("users-card-deck").appendChild(document.getElementById("card_" + id));
        id = id + 1;
    }
}