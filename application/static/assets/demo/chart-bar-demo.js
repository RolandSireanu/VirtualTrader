// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';



// Bar Chart Example
var ctx = document.getElementById("myBarChart");

async function GetCryptoFromApi2(){

  let resp = await fetch(`${window.origin}/api?crypto=all`,{
    method: "GET",
    credentials: "include",
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  });

  console.log(resp);

  if(resp.status === 200){
    data = await resp.json();
    return data;
  }
  else
  {
    return null;
  }
}

function BuildBarChart(){
  GetCryptoFromApi2().then(
    function(dataObject){
      var myLineChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: Object.keys(dataObject),
          datasets: [{
            label: "Revenue",
            backgroundColor: "rgba(2,117,216,1)",
            borderColor: "rgba(2,117,216,1)",
            data: Object.values(dataObject)
          }],
        },
        options: {
          scales: {
            xAxes: [{
              time: {
                unit: 'month'
              },
              gridLines: {
                display: false
              },
              ticks: {
                maxTicksLimit: 6
              }
            }],
            yAxes: [{
              ticks: {
                min: 0,
                max: 100,
                maxTicksLimit: 5
              },
              gridLines: {
                display: true
              }
            }],
          },
          legend: {
            display: false
          }
        }
      })
    }
  );
}

// GetCryptoFromApi2().then(function(data){
//   console.log(data);
// });

// async function GetCryptoFromApi(){

//   let ret;

//   let r = fetch(`${window.origin}/api?crypto=all`,{
//     method: "GET",
//     credentials: "include",
//     cache: "no-cache",
//     headers: new Headers({
//       "content-type": "application/json"
//     })
//   }).then(function(resp){
//     if(resp.status !== 200){
//       console.log("Returned status not ok !");
//       return ;
//     }

//     resp.json().then(function (dataObject){
//       //console.log(dataObject)
//       var myLineChart = new Chart(ctx, {
//         type: 'bar',
//         data: {
//           labels: Object.keys(dataObject),
//           datasets: [{
//             label: "Revenue",
//             backgroundColor: "rgba(2,117,216,1)",
//             borderColor: "rgba(2,117,216,1)",
//             data: Object.values(dataObject)
//           }],
//         },
//         options: {
//           scales: {
//             xAxes: [{
//               time: {
//                 unit: 'month'
//               },
//               gridLines: {
//                 display: false
//               },
//               ticks: {
//                 maxTicksLimit: 6
//               }
//             }],
//             yAxes: [{
//               ticks: {
//                 min: 0,
//                 max: 15000,
//                 maxTicksLimit: 5
//               },
//               gridLines: {
//                 display: true
//               }
//             }],
//           },
//           legend: {
//             display: false
//           }
//         }
//       });
//     });
//   });
// }

// GetCryptoFromApi();
BuildBarChart();

