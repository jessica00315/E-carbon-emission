// 模擬資料
const monthlyData = {
  labels: ['1月', '2月', '3月', '4月', '5月', '6月'],
  datasets: [{
    label: '碳排放量（tCO₂e）',
    data: [120, 132, 128, 142, 139, 125],
    backgroundColor: '#3498db'
  }]
};

const pieDataPlant = {
  labels: ['冬山廠', '羅東廠', '宜蘭廠'],
  datasets: [{
    data: [40, 35, 25],
    backgroundColor: ['#2ecc71', '#e67e22', '#9b59b6']
  }]
};

const pieDataProcess = {
  labels: ['原料熔融', '成型', '包裝', '物流'],
  datasets: [{
    data: [50, 30, 15, 5],
    backgroundColor: ['#f1c40f', '#2980b9', '#e74c3c', '#1abc9c']
  }]
};

const intensityData = {
  labels: ['1月', '2月', '3月', '4月', '5月', '6月'],
  datasets: [{
    label: 'kgCO₂e / kg成品',
    data: [2.4, 2.3, 2.1, 2.2, 2.0, 1.9],
    borderColor: '#e67e22',
    backgroundColor: 'rgba(230,126,34,0.1)',
    fill: true,
    tension: 0.3
  }]
};

const renewableData = {
  labels: ['綠電占比'],
  datasets: [{
    label: '使用占比',
    data: [35],
    backgroundColor: ['#2ecc71']
  }]
};

const ctx1 = document.getElementById('monthlyEmissionChart');
new Chart(ctx1, {
  type: 'bar',
  data: monthlyData,
  options: { responsive: true }
});

new Chart(document.getElementById('plantEmissionPie'), {
  type: 'pie',
  data: pieDataPlant,
  options: { responsive: true }
});

new Chart(document.getElementById('processEmissionPie'), {
  type: 'pie',
  data: pieDataProcess,
  options: { responsive: true }
});

new Chart(document.getElementById('intensityChart'), {
  type: 'line',
  data: intensityData,
  options: { responsive: true }
});

new Chart(document.getElementById('renewableChart'), {
  type: 'bar',
  data: renewableData,
  options: {
    indexAxis: 'y',
    responsive: true,
    plugins: { legend: { display: false } }
  }
});
