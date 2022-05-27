/**
 * This function takes a dictionary
 * and cleans up its Dates to make it ready to 
 * be visualized
 * @param {*} dictionary_inside_array 
 * @returns an array with cleaned json inside
 */
function clean_dates_in_dictionary(dictionary_inside_array){
    
    cleaned_dictionary_inside_array = JSON.parse(dictionary_inside_array);

    
    var new_arr = new Array();

    for (var i = 0; i < cleaned_dictionary_inside_array.length; i++){
        var cur = cleaned_dictionary_inside_array[i];
        cur['x'] = new Date(cur['x'])


        new_arr.push(cur);

    }

    return new_arr;
}

/**
 * Takes the arrays portfolio returns and benchmark returns
 * visualizes them with chart.js
 * 
 */
function show_chart(json_dictionary_port_returns, json_dictionary_benchmark_returns) {
    // console.log(json_dictionary_port_returns);
    // console.log(json_dictionary_benchmark_returns);
    cleaned_json_dictionary_port_returns =  clean_dates_in_dictionary(json_dictionary_port_returns);
    cleaned_json_dictionary_benchmark_returns =  clean_dates_in_dictionary(json_dictionary_benchmark_returns);

    console.log(cleaned_json_dictionary_port_returns);

    
    var chart = new CanvasJS.Chart("chartContainer", {
        title: {
            text: "Portfolio vs Benchmark Returns"
        },
        axisX: {
            valueFormatString: "MMM DD YYYY"
        },
        axisY2: {
            title: "Percentage Returns (new-old)/old"
        },
        toolTip: {
            shared: true
        },
        // legend: {
        //     cursor: "pointer",
        //     verticalAlign: "top",
        //     horizontalAlign: "center",
        //     dockInsidePlotArea: true,
        //     itemclick: toogleDataSeries
        // },
        data: [{
            type: "line",
            axisYType: "secondary",
            name: "Portfolio Returns",
            showInLegend: true,
            markerSize: 0,
            // yValueFormatString: "$#,###k",
            dataPoints: cleaned_json_dictionary_port_returns
            // new Array({x: new Date("2018-11-19"), y: 5}
            //           ,{x: new Date("2018-11-20"), y: 3}
            //           ,{x: new Date("2018-11-21"), y: 4})
        },
        {
            type: "line",
            axisYType: "secondary",
            name: "Benchmark Returns",
            showInLegend: true,
            markerSize: 0,
            // yValueFormatString: "$#,###k",
            dataPoints: cleaned_json_dictionary_benchmark_returns
            // new Array({x: new Date("2018-11-19"), y: 7}
            //           ,{x: new Date("2018-11-20"), y: 3}
            //           ,{x: new Date("2018-11-21"), y: 2})

        },
        ]

    });
    chart.render();


}