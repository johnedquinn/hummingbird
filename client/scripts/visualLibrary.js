// @file   : visualLibrary.js
// @author : John Ed Quinn
// @desc   : JS file to render items

// @func : Item
// @desc : N/A
function Item () {
    this.addToDocument = function () {
        document.body.appendChild(this.item);
    }
}

// @func : Label
// @desc : N/A
function Label () {
    this.createLabel = function (body, id) {
        this.item = document.createElement("h4");
        this.item.setAttribute("id", id);
        this.setText(body);
    }
    this.setText = function (body) {
        this.item.innerHTML = body;
    }
}

// @func : Button
// @desc : N/A
function Button () {
    this.createButton = function (body, id) {
        this.item = document.createElement("button");
        this.item.setAttribute("id", id);
        this.item.setAttribute("class", "btn btn-info");
        var itemBody = document.createTextNode(body);
        this.item.appendChild(itemBody);
        document.body.appendChild(this.item);
    }
    this.addClickEventHandler = function (handler) {
        this.item.onmouseup = function () {
            handler();
        }
    }
}

// @func : Dropdown
// @desc : N/A
function Dropdown () {
    this.createDropdown = function (dict, id, selected) {
        this.item = document.createElement("select");
        this.item.setAttribute("id", id);
        // Add all items
        for (var key in dict) {
            option = document.createElement("option");
            option.setAttribute("value", key);
            option.innerHTML = dict[key];
            this.item.appendChild(option);
        }
    }
    this.getSelected = function () {
        var selected = document.getElementById("rating_dropdown").value;
        var selected = parseFloat(selected) + 1;
        return selected;
    }
}

// @func : Div
// @desc : N/A
function Div (id, className) {
    div = document.createElement("div");
    div.setAttribute("id", id);
    div.setAttribute("class", className);
    document.body.appendChild(div);
    this.appendToDiv = function (child_name) {
        child_div = document.getElementById(child_name);
        div.appendChild(child_div);
    }
}

// @func : Card
// @desc 
function Card (id, title, subtitle, text, num) {

    // Body Div
    var body_div = new Div("card_body_" + id, "card-body");
    
    // Grab Title Label
    if (title) {
        var title_label = document.createElement("h5");
        title_label.setAttribute("class", "card-title");
        title_label.setAttribute("id", "card_title_label_" + id);
        title_label.innerHTML = title;
        document.body.appendChild(title_label);
        body_div.appendToDiv("card_title_label_" + id);
    }
    if (num){
        var num_label = document.createElement("h6");
        num_label.setAttribute("class", "card-number");
        num_label.setAttribute("id", "card_num_label_" + id);
        num = "Holdings: " + num;
        num_label.innerHTML = num;
        document.body.appendChild(num_label);
        body_div.appendToDiv("card_num_label_" + id);
    }

    // Subtitle Label
    if (subtitle) {
        var subtitle_label = document.createElement("small");
        subtitle_label.setAttribute("id", "card_subtitle_" + id);
        subtitle_label.setAttribute("class", "text_muted");
        subtitle_label.innerHTML = subtitle;
        document.body.appendChild(subtitle_label);
        body_div.appendToDiv("card_subtitle_" + id);
    }

    // Text Label
    if (text) {
        var color = "text-success";
        if (text.toString().indexOf('-') > -1) {
            color = "text-danger";
        }
        var text_label = document.createElement("p");
        text_label.setAttribute("class", "card-text " + color);
        text_label.setAttribute("id", "card_text_label_" + id);
        text_label.innerHTML = text;
        document.body.appendChild(text_label);
        body_div.appendToDiv("card_text_label_" + id);
    }


    // Create Card
    var card = new Div("card_" + id, "card");
    card.appendToDiv("card_body_" + id);
}

// @func : Image
// @desc : N/A
function Image (id) {
    image = document.createElement("img");
    image.setAttribute("id", id);
    document.body.appendChild(image);

    // @func : updateImage
    // @desc : updates the source for the image
    this.updateImage = function (img) {
        image.setAttribute("src", "http://student04.cse.nd.edu/skumar5/images" + img);
    }
}

Label.prototype = new Item();
Button.prototype = new Item();
Dropdown.prototype = new Item();
Div.prototype = new Item();
Image.prototype = new Item();
Card.prototype = new Item();