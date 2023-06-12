// login.js
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/login.py');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                alert('Login successful');
                // Redirecionar para a página de destino após o login bem-sucedido
                window.location.href = '/dashboard';
            } else {
                alert('Invalid credentials');
            }
        }
    };

    var data = JSON.stringify({
        username: username,
        password: password
    });
    xhr.send(data);
});