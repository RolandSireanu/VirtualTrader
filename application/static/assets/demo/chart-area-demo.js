// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

async function getDataFromAPI(coin) {
  let startPoint = Math.floor((Date.now() / 1000)) - (3600*24*30)

  while(true){
    
    response = await fetch("https://coingecko.p.rapidapi.com/coins/"+coin+"/market_chart/range?from="+String(startPoint)+"&vs_currency=usd&to="+String(Date.now()), {
        "method": "GET",
        "headers": {
            "x-rapidapi-key": "1057bfb784msh8fa5180c3b466bdp1802bcjsnf6263a56e4b1",
            "x-rapidapi-host": "coingecko.p.rapidapi.com"
        }
        });
    
    if (response.ok == true) {
        break;
    }
    else
    {
        await new Promise(resolve => setTimeout(resolve, 5000));
        console.log("Coins API fail  ")
    }
  }
    return response;
}

async function getData(coin){

  
  let response = null
  let ok = false;

  
    try {         
      response = await getDataFromAPI(coin)
    }catch(e){
      console.log("Erro from server !!! ");
      console.log(e)
    }



  let data = await response.json();
  
  let values = [];
  let date = [];

  for(i=0; i<data["prices"].length; i++){
    // val = Math.floor(data["prices"][i][1]);
    val = parseFloat(data["prices"][i][1]).toFixed(2);
    values.push(val > 0 ? val : parseFloat(data["prices"][i][1]).toFixed(2));

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

function getNearest(nr, direction){
  let base = 1;
  let temp = nr;
  console.log("getNearest : " + nr);
  while(temp > 10){
    base = base*10;
    temp = Math.floor(nr / base);
  }

  if(direction == "Up"){
    if(nr < 1) return 1;
    return (temp*base)+base;
  }
  else if(direction == "Down"){
    return (temp*base);
  }

}


let nodes = Array.from(document.querySelectorAll('[id$="-AreaChart"]')).map(function (item){ return item.id; });
var lineCharts = [...Array(nodes.length)];
console.log(nodes);
for (let i=0; i<nodes.length; i++){
  console.log(nodes[i]);
  let ctx = document.getElementById(nodes[i]);
  console.log(ctx);


  getData(nodes[i].split("-")[0]).then(function(data){
    console.log(data);
    
    let max = Math.max.apply(Math, data["v"]);
    let min = Math.min(...data["v"]);

    lineCharts[i] = new Chart(ctx, {
      type: 'line',
      data: {
        labels: data["d"],//["Mar 1", "Mar 3", "Mar 4", "Mar 5", "Mar 6", "Mar 7", "Mar 8", "Mar 9", "Mar 10", "Mar 11", "Mar 12", "Mar 13"],
        datasets: [{
          label: "Price",
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
              maxTicksLimit: 30
            }
          }],
          yAxes: [{
            ticks: {
              min: getNearest(min, "Down"),
              max: getNearest(max, "Up"), //Math.max.apply(Math, data["v"]),
              maxTicksLimit: 10
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
}