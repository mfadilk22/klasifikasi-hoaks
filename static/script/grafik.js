// const Chart = require('chart.js');
// document.querySelector(".hasil_prediksi");
var hasil_prediksi = document.querySelector(".hasil_prediksi");
var hasil_hoaks = Number(hasil_prediksi.dataset.prediksi);
var hasil_non_hoaks = 100 - hasil_hoaks;
var ctx = document.getElementById("myChart");

const datachart = {
    labels: [
        "Hoaks",
        'Tidak Hoaks',
      ],
      datasets: [{
        label: 'My First Dataset',
        data: [hasil_hoaks, hasil_non_hoaks],
        backgroundColor: [
          'rgb(252, 81, 121)',
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

if (hasil_non_hoaks == 100){
  ctx.style.display = 'none';
}
else{
  ctx.style.display = 'flex';
}