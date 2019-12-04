// @file : scripts/index_charts.js
// @desc : creates the chart for the index page

// Create chart on load
var chart;
var symbol_chart = JSON.parse(get_chart("KOD"));
create_index_chart();

// @func : get_chart
// @desc : gets the chart data for one symbol
function get_chart (symbol) {
    var r = new XMLHttpRequest();
    r.open("GET", "http://student04.cse.nd.edu:51075/charts/" + symbol, false);
    r.onload = function (e) {
        //console.log(r.responseText);
    }
    r.onerror = function (e) {
        console.error(r.statusText);
    }
    r.send(null);
    return r.responseText;
}

// @func : create_index_chart
// @desc : searches for the chart and updates it
function create_index_chart() {
    var ctx = document.getElementById('myChart').getContext('2d');
    var times = symbol_chart["timestamp"];
    times = times.map(function (num) { return num * 1000; });
    console.log(times);
    var open_data = symbol_chart["open"];
    chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: times,
            datasets: [{
                label: 'Your Holdings',
                borderColor: 'rgb(92,184,92)',
                tension: 0,
                fill: false,
                hitRadius: 4,
                data: open_data,
                pointRadius: 1
            }]
        },
        options: {
            legend: {
                display: false
            },
            scales: {
                xAxes: [{
                    /*type: 'time',
                    time: {
                        unit: 'day',
                    },*/
                    /*afterBuildTicks: function (chart) {
                        chart.ticks = []
                        for (i = 0; i < times.length; i++) {
                            if (i % 15 == 0) chart.ticks.push(times[i]);
                            else chart.ticks.push(0);
                        }
                    }*/
                }]
            }
        }
    });
}