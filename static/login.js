// login.js
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/login'); 
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                if (response.message === 'Login successful') {
                    alert('Login successful');
                    window.location.href = '/dashboard.html';

                } else {
                    alert('Invalid credentials');
                }
            } else if (xhr.status === 401) {
                alert('Invalid credentials');
            } else {
                alert('An error occurred. Please try again later.');
            }
        }
    };

    var data = JSON.stringify({
        username: username,
        password: password
    });
    xhr.send(data);
});