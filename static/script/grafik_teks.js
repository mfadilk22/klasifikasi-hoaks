// const Chart = require('chart.js');
// document.querySelector(".hasil_prediksi");
var hasil_prediksi_teks = document.querySelector(".hasil_prediksi_teks");
var hasil_hoaks_teks = Number(hasil_prediksi_teks.dataset.prediksi);
var hasil_non_hoaks_teks = 100 - hasil_hoaks_teks;
var ctx1 = document.getElementById("myChart");
// var ctx2 = document.getElementById("myChart2");

const datachart_teks = {
    labels: [
        "Hoaks",
        'Tidak Hoaks',
      ],
      datasets: [{
        label: 'My First Dataset',
        data: [hasil_hoaks_teks, hasil_non_hoaks_teks],
        backgroundColor: [
          'rgb(252, 81, 121)',
          'rgb(54, 162, 235)',
        ],
        hoverOffset: 4
      }]
}

const config_teks = {
  type: 'doughnut',
  data: datachart_teks,
  options: {
    responsive: true,
  },
}
const myChart = new Chart(ctx1, config_teks);

if (hasil_non_hoaks_teks == 100){
  ctx1.style.display = 'none';
}
else{
  ctx1.style.display = 'flex';
}

// if (hasil_non_hoaks == 100){
//   ctx2.style.display = 'none';
// }
// else{
//   ctx2.style.display = 'flex';
// }