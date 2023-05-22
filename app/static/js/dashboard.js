/* globals Chart:false, feather:false */

(function () {
    'use strict'
  
    feather.replace()
  
    // Get the chart canvas element
    var ctx = document.getElementById('myChart')
  
    // Fetch the data from the server using an API endpoint (replace 'api/entries' with the actual endpoint URL)
    fetch('/api/entries')
      .then(function (response) {
        return response.json()
      })
      .then(function (data) {
        // Process the retrieved data
        var labels = data.map(function (entry) {
          // Extract the date part from the entry's date
          return entry.date.split('T')[0]
        })
  
        var weights = data.map(function (entry) {
          // Extract the weight from each entry
          return entry.weight
        })
  
        // Create the chart using the retrieved data
        var myChart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: labels,
            datasets: [{
              data: weights,
              lineTension: 0,
              backgroundColor: 'transparent',
              borderColor: '#007bff',
              borderWidth: 4,
              pointBackgroundColor: '#007bff'
            }]
          },
          options: {
            scales: {
              yAxes: [{
                ticks: {
                  beginAtZero: false
                }
              }]
            },
            legend: {
              display: false
            }
          }
        })
      })
      .catch(function (error) {
        console.log(error)
      })
  })()
  