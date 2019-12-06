// @file : scripts/profile_charts.js
// @desc : creates the chart for the index page

// @func : create_user_networth_chart
// @desc : creates the chart on the account page
function create_user_networth_chart (user) {
    var stocks = user["stocks"];
    var times = [];
    var open_values = [];
    for (symbol in stocks) {
        var chart = JSON.parse(get_chart(symbol));
        var current_times = chart["timestamp"];
        var current_values = chart["open"];
        var amount = stocks[symbol];
        var updated_values = current_values.map(function (num) { return num * amount; });
        if (open_values.length == 0) {
            open_values = current_values;
            times = current_times;
        } else {
            for (i = 0; i < open_values.length; i++) {
                if (i >= updated_values.length) break;
                open_values[i] += updated_values[i];
            }
        }
    }
    create_chart("networth_chart", times, open_values);
}