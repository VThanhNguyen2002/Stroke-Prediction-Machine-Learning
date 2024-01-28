// Lấy tất cả các phần tử có class "counter"
const counters = document.querySelectorAll('.counter');

// Lặp qua từng phần tử và thực hiện hiệu ứng số đếm
counters.forEach(counter => {
    const target = +counter.getAttribute('data-count');
    let count = 1;
    const increment = target / 100; // Điều chỉnh tốc độ tăng số

    const updateCount = () => {
        count += increment;
        if (count < target) {
            counter.textContent = Math.ceil(count);
            setTimeout(updateCount, 10); // Điều chỉnh tốc độ cập nhật số
        } else {
            counter.textContent = target;
        }
    };

    updateCount();
});


// Biểu đồ đo lường
const labels = ['January', 'February', 'March', 'April', 'May', 'June']

const data = {
  labels: labels,
  datasets: [
    {
      label: 'Tổng số bệnh nhân',
      backgroundColor: '#e74c3c',
      borderColor: '#e74c3c',
      data: [10, 27, 56, 34, 24, 53],
      tension: 0.4,
    },
    {
      label: 'Người mắc bệnh đột quỵ',
      backgroundColor: '#2ecc71',
      borderColor: '#2ecc71',
      data: [0, 34, 32, 23, 2, 82],
      tension: 0.4,
    },
  ],
}
const config = {
  type: 'line',
  data: data,
}

const canvas = document.getElementById('canvas')
const chart = new Chart(canvas, config)

//Thông báo yêu cầu đăng nhập
function showCustomAlert() {
  Swal.fire({
    title: 'Thông báo !',
    text: 'Vui lòng đăng nhập',
    icon: 'info',
    confirmButtonText: 'OK'
  });
}

//Hiện mật khẩu
function togglePassword() {
  var passwordField = document.getElementById("password");
  if (passwordField.type === "password") {
    passwordField.type = "text";
  } else {
    passwordField.type = "password";
  }
}