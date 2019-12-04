// @file   : main.js
// @author : John Ed Quinn
// @desc   : JS file to use visualLibrary

/* Runtime Execution */

// Grab Initial Data
var mid = 5;
var data = get_all_data(mid);

// Add Center Movie Title
var title_label = new Label();
title_label.createLabel(data["title"], "title_label");
title_label.addToDocument();
var title_div = new Div("title_div", "container");
title_div.appendToDiv("title_label");

// Add Center Movie Image
var movie_image = new Image("movie_image");
movie_image.updateImage(data["img"]);
var movie_image_div = new Div("movie_image_div", "container");
movie_image_div.appendToDiv("movie_image");

// Add Center Rating Information
var rating_label = new Label();
rating_label.createLabel(data["rating"], "rating_label");
rating_label.addToDocument();
var rating_div = new Div("rating_div", "container");
rating_div.appendToDiv("rating_label");

// Add UP Button
var up_button = new Button();
up_button.createButton("UP", "up_button");
up_button.addToDocument();
var up_button_div = new Div("up_button_div", "container");
up_button_div.appendToDiv("up_button");

// Add UP Button
var down_button = new Button();
down_button.createButton("DOWN", "down_button");
//down_button.addToDocument();
var down_button_div = new Div("down_button_div", "container");
down_button_div.appendToDiv("down_button");

// Create Columns
var middle_column = new Div("middle_column", "col col-6");
middle_column.appendToDiv("title_div");
middle_column.appendToDiv("movie_image_div");
middle_column.appendToDiv("rating_div");

var left_column = new Div("left_column", "col col-3 d-flex align-items-center");
left_column.appendToDiv("down_button_div");

var right_column = new Div("right_column", "col col-3 d-flex align-items-center");
right_column.appendToDiv("up_button_div");

var page = new Div("page", "row");
page.appendToDiv("left_column");
page.appendToDiv("middle_column");
page.appendToDiv("right_column");

var entire_page = new Div("entire_page", "container");
entire_page.appendToDiv("page");


/* Post-Runtime Execution */

// Add Click Event Handlers

// Up Button Clicker
up_button.addClickEventHandler(up_rate);

// Down Button Clicker
down_button.addClickEventHandler(down_rate);

// @func : up_rate
// @desc : up rate movie and update UI
function up_rate () {
    add_rating(mid, 5);
    mid = get_next_mid(mid);
    data = get_all_data(mid);
    update_content(data);
}

// @func : down_rate
// @desc : down rate movie and update UI
function down_rate () {
    add_rating(mid, 1);
    mid = get_next_mid(mid);
    data = get_all_data(mid);
    update_content(data);
}

// @func : get_next_mid
// @desc : gets next recommended movie
function get_next_mid (mid) {
    var mid_data = JSON.parse(get_data("http://student04.cse.nd.edu:51075/ratings/next/", 100));
    console.log(mid_data);
    return parseInt(mid_data["mid"]);
}

// @func : make_queries
// @desc : get movie and rating info and update labels
function get_all_data (mid) {

    // Local Variables
    var data = {};
    var movie_data = JSON.parse(get_data("http://student04.cse.nd.edu:51075/movies/", mid.toString()));
    var rating_data = JSON.parse(get_data("http://student04.cse.nd.edu:51075/ratings/", mid.toString()));

    console.log(movie_data);

    // Parse Data
    data["mid"] = movie_data["id"];
    data["img"] = movie_data["img"];
    data["title"] = movie_data["title"];
    data["rating"] = rating_data["rating"];
    return data;
}

// @func : get_data
// @desc : gets data from server
function get_data (url, mid) {
    var r = new XMLHttpRequest();
    r.open("GET", url + mid, false);
    r.onload = function (e) {
        console.log(r.responseText);
    }
    r.onerror = function (e) {
        console.error(r.statusText);
    }
    r.send(null);
    return r.responseText;
}

// @func : add_rating
// @desc : send own rating
function add_rating (mid, rating) {
    var r = new XMLHttpRequest();
    r.open("PUT", "http://student04.cse.nd.edu:51075/recommendations/100", true);
    var target = { "movie_id": mid, "rating": rating };
    r.send(JSON.stringify(target));
    r.onload = function (e) {
        console.log(r.responseText);
    } 
    r.onerror = function (e) {
        console.log(r.rstatusText);
    }
}

// @func : update_content
// @desc : update the UI
function update_content (data) {
    title_label.setText(data["title"]);
    rating_label.setText(data["rating"]);
    movie_image.updateImage(data["img"]);
}