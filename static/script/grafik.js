const Chart = require('chart.js');
let hasil_prediksi = parseFloat(document.querySelector(".hasil_prediksi"));
let ctx = document.getElementById("myChart")

const datachart = {
    labels: [
        'Hoaks',
        'Tidak Hoaks',
      ],
      datasets: [{
        label: 'My First Dataset',
        data: [hasil_prediksi, 100-hasil_prediksi],
        backgroundColor: [
          'rgb(255, 205, 86)',
          'rgb(54, 162, 235)',
        ],
        hoverOffset: 4
      }]
}
const myChart = new Chart(ctx, {
    type: 'doughnut',
    data: datachart,
});