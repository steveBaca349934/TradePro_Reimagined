function clean_dates_in_dictionary(dictionary_inside_array){

    // iterate through the dictionary contained in the array
    // for (var i = 0; i < dictionary_inside_array.length; i++){

    //     cur_d = dictionary_inside_array[i];
    //     console.log(i);
    //     console.log(cur_d);

    // }
    // dictionary_inside_array.forEach(myFunction);
    // console.log("\n \n \n \n the type of dictionary inside array is ")
    // For whatever reason javascript currently thinks that the 
    // dictionary_inside_array is a type string
    cleaned_dictionary_inside_array = JSON.parse(dictionary_inside_array);

    // console.log("\n \n \n \n the type of dictionary inside array after cleaning is: ")
    // console.log(typeof cleaned_dictionary_inside_array);

    // for (var i = 0; i < cleaned_dictionary_inside_array.length; i++){
    //     var cur = cleaned_dictionary_inside_array[i];

    //     console.log(i);
    //     console.log(cur);
    // }
    var new_arr = new Array();

    for (var i = 0; i < cleaned_dictionary_inside_array.length; i++){
        var cur = cleaned_dictionary_inside_array[i];
        cur['x'] = new Date(cur['x'])


        new_arr.push(cur);

    }

    return new_arr;
}

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