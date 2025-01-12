$(() => {
  $("#register-form").on("submit", function (event) {
    event.preventDefault();
    const formData = {};
    $(this).serializeArray().forEach(field => {
        formData[field.name] = field.value;
    });

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
