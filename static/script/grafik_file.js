// const Chart = require('chart.js');
// document.querySelector(".hasil_prediksi");
var hasil_prediksi_file = document.querySelector(".hasil_prediksi_file");
var hasil_hoaks_file = Number(hasil_prediksi_file.dataset.prediksi);
var hasil_non_hoaks_file = 100 - hasil_hoaks_file;
// var ctx1 = document.getElementById("myChart");
var ctx2 = document.getElementById("myChart2");

const datachart_file = {
    labels: [
        "Hoaks",
        'Tidak Hoaks',
      ],
      datasets: [{
        label: 'My First Dataset',
        data: [hasil_hoaks_file, hasil_non_hoaks_file],
        backgroundColor: [
          'rgb(252, 81, 121)',
          'rgb(54, 162, 235)',
        ],
        hoverOffset: 4
      }]
}

const config_file = {
  type: 'doughnut',
  data: datachart_file,
  options: {
    responsive: true,
  },
}

const myChart2 = new Chart(ctx2, config_file);

if (hasil_non_hoaks_file == 100){
  ctx2.style.display = 'none';
}
else{
  ctx2.style.display = 'flex';
}