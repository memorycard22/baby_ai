document.getElementById('listen-btn').addEventListener('click', function() {
    const responseElement = document.getElementById('response');
    responseElement.textContent = 'Listening...';

    fetch('http://192.168.31.246:5000/listen')  // Replace with your correct IP address
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            responseElement.textContent = data.command;
        })
        .catch(error => {
            responseElement.textContent = 'Error: ' + error;
        });
});
