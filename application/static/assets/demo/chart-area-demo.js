// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

async function getData(){

  let startPoint = Math.floor((Date.now() / 1000)) - (3600*24*30)
  console.log(startPoint);

  let response = await fetch("https://coingecko.p.rapidapi.com/coins/bitcoin/market_chart/range?from="+String(startPoint)+"&vs_currency=usd&to="+String(Date.now()), {
    "method": "GET",
    "headers": {
      "x-rapidapi-key": "1057bfb784msh8fa5180c3b466bdp1802bcjsnf6263a56e4b1",
      "x-rapidapi-host": "coingecko.p.rapidapi.com"
    }
  });

  let data = await response.json();
  let values = [];
  let date = [];

  for(i=0; i<data["prices"].length; i++){
    values.push(Math.floor(data["prices"][i][1]));

    let t = new Date(Math.floor(data["prices"][i][0]));
    tempData = t.toLocaleString("en-US", {month: "long"}) + t.toLocaleString("en-US", {day: "numeric"});
    // console.log(t.toLocaleString("en-US", {month: "long"}) + t.toLocaleString("en-US", {day: "numeric"}))
    date.push(tempData);
  }

  return {
    v : values,
    d : date
  }
}



getData().then(function(data){
  console.log(data);
  var ctx = document.getElementById("myAreaChart");
  var myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: data["d"],//["Mar 1", "Mar 3", "Mar 4", "Mar 5", "Mar 6", "Mar 7", "Mar 8", "Mar 9", "Mar 10", "Mar 11", "Mar 12", "Mar 13"],
      datasets: [{
        label: "Sessions",
        lineTension: 0.3,
        backgroundColor: "rgba(2,117,216,0.2)",
        borderColor: "rgba(2,117,216,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(2,117,216,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(2,117,216,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: data["v"]//[10000, 30162, 26263, 18394, 18287, 28682, 31274, 33259, 25849, 24159, 32651, 31984, 38451],
      }],
    },
    options: {
      scales: {
        xAxes: [{
          time: {
            unit: 'date'
          },
          gridLines: {
            display: false
          },
          ticks: {
            maxTicksLimit: 7
          }
        }],
        yAxes: [{
          ticks: {
            min: 40000,
            max: 80000, //Math.max.apply(Math, data["v"]),
            maxTicksLimit: 5
          },
          gridLines: {
            color: "rgba(0, 0, 0, .125)",
          }
        }],
      },
      legend: {
        display: false
      }
    }
  });
});

// Area Chart Example

// var myLineChart = new Chart(ctx, {
//   type: 'line',
//   data: {
//     labels: [],//["Mar 1", "Mar 3", "Mar 4", "Mar 5", "Mar 6", "Mar 7", "Mar 8", "Mar 9", "Mar 10", "Mar 11", "Mar 12", "Mar 13"],
//     datasets: [{
//       label: "Sessions",
//       lineTension: 0.3,
//       backgroundColor: "rgba(2,117,216,0.2)",
//       borderColor: "rgba(2,117,216,1)",
//       pointRadius: 5,
//       pointBackgroundColor: "rgba(2,117,216,1)",
//       pointBorderColor: "rgba(255,255,255,0.8)",
//       pointHoverRadius: 5,
//       pointHoverBackgroundColor: "rgba(2,117,216,1)",
//       pointHitRadius: 50,
//       pointBorderWidth: 2,
//       data: [10000, 30162, 26263, 18394, 18287, 28682, 31274, 33259, 25849, 24159, 32651, 31984, 38451],
//     }],
//   },
//   options: {
//     scales: {
//       xAxes: [{
//         time: {
//           unit: 'date'
//         },
//         gridLines: {
//           display: false
//         },
//         ticks: {
//           maxTicksLimit: 7
//         }
//       }],
//       yAxes: [{
//         ticks: {
//           min: 0,
//           max: 100000,
//           maxTicksLimit: 5
//         },
//         gridLines: {
//           color: "rgba(0, 0, 0, .125)",
//         }
//       }],
//     },
//     legend: {
//       display: false
//     }
//   }
// });
