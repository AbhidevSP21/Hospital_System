// Dummy data for metrics
document.getElementById("totalDepartments").innerText = 8;
document.getElementById("totalDoctors").innerText = 14;
document.getElementById("totalPatients").innerText = 1;
document.getElementById("totalAppointments").innerText = 3;

// Charts using Chart.js
const monthlyRegisteredUsersCtx = document.getElementById('monthlyRegisteredUsersChart').getContext('2d');
const monthlyRegisteredUsersChart = new Chart(monthlyRegisteredUsersCtx, {
    type: 'bar',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
        datasets: [{
            label: 'Monthly Registered Users',
            data: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
            backgroundColor: 'rgba(0, 123, 255, 0.2)',
            borderColor: 'rgba(0, 123, 255, 1)',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});

const earningsCtx = document.getElementById('earningsChart').getContext('2d');
const earningsChart = new Chart(earningsCtx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
        datasets: [{
            label: 'Earnings ($)',
            data: [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500],
            backgroundColor: 'rgba(40, 167, 69, 0.2)',
            borderColor: 'rgba(40, 167, 69, 1)',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});
