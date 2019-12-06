
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
function create_chart(chart_id, xAxis, yAxis) {
    var ctx = document.getElementById(chart_id).getContext('2d');
    // Change epoch to time strings
    var modified_xAxis = xAxis.map(function(num) {
        var date = new Date(0);
        date.setUTCSeconds(num);
        return date.getHours().toString() + ":" + date.getMinutes().toString();
    });
    // Create chart
    chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: modified_xAxis,
            datasets: [{
                label: 'Your Holdings',
                borderColor: 'rgb(92,184,92)',
                tension: 0,
                fill: false,
                hitRadius: 4,
                data: yAxis,
                pointRadius: 1
            }]
        },
        options: {
            legend: {
                display: false
            },
            scales: {
                xAxes: [{
                    afterBuildTicks: function (chart) {
                        chart.ticks = []
                        for (i = 0; i < modified_xAxis.length; i++) {
                            if (i % 2 == 0) chart.ticks.push(modified_xAxis[i]);
                            else chart.ticks.push(" ");
                        }
                    }
                }]
            },
            title: {
                display: true,
                text: 'Your Investments over 24 Hours'
            }
        }
    });
}