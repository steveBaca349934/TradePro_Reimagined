function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function show_chart(json_dictionary_port_returns, json_dictionary_benchmark_returns) {
    console.log(json_dictionary_port_returns);
    console.log(json_dictionary_benchmark_returns);

    var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        theme: "light2",
        title: {
            text: "Simple Line Chart"
        },
        datasets: [{
            label: "Portfolio Returns",
            //fill:false,
            fillColor: "rgba(0,0,0,0)",
            strokeColor: "rgba(220,220,220,1)",
            pointColor: "rgba(200,122,20,1)",

            data: json_dictionary_port_returns
        },
        {
            label: "Benchmark Returns",
            fillColor: 'rgba(0,0,0,0)',
            strokeColor: 'rgba(220,180,0,1)',
            pointColor: 'rgba(220,180,0,1)',
            data: json_dictionary_benchmark_returns
        }]
    });
    chart.render();
}