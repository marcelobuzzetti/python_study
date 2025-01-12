$(() => {
  $("#register-form").on("submit", function (event) {
    event.preventDefault();
    const formData = {
        username: document.getElementById('username').value,
        display_name: document.getElementById('display_name').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value
    };

    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    });
  });
});
