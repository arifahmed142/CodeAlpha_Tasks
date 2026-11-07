document.addEventListener('DOMContentLoaded', function() {
    const password = document.getElementById('password');
    const confirm_password = document.getElementById('confirm_password');
    const message = document.getElementById('message');
    const form = document.querySelector('form');

    function checkPassword() {
        if (confirm_password.value === '') {
            message.textContent = '';
        }
        else if (password.value === confirm_password.value) {
            message.textContent = 'Passwords match!';
            message.style.color = 'green';
        }
        else {
            message.textContent = 'Passwords do not match!';
            message.style.color = 'red';
        }
    }

    password.addEventListener('input', checkPassword);
    confirm_password.addEventListener('input', checkPassword);

    form.addEventListener('submit', function(event) {
        if (password.value !== confirm_password.value) {
            event.preventDefault();
            message.textContent = 'Passwords do not match!';
            message.style.color = 'red';
        }
    });
});
