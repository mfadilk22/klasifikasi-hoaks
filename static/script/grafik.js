// const Chart = require('chart.js');

var hasil_prediksi = document.querySelector(".hasil_prediksi");
var hasil = Number(hasil_prediksi)
var ctx = document.getElementById("myChart");

const datachart = {
    labels: [
        hasil_prediksi,
        'Tidak Hoaks',
      ],
      datasets: [{
        label: 'My First Dataset',
        data: [60, 100-60],
        backgroundColor: [
          'rgb(255, 205, 86)',
          'rgb(54, 162, 235)',
        ],
        hoverOffset: 4
      }]
}

const config = {
  type: 'doughnut',
  data: datachart,
  options: {
    responsive: true,
  },
}
const myChart = new Chart(ctx, config);