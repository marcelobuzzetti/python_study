$(() => {
  $("#register-form").on("submit", function (event) {
    event.preventDefault();
    formData = Object.fromEntries(new FormData(event.target))  
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
