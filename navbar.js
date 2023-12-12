// navbar.js
document.addEventListener('DOMContentLoaded', function () {
    // Get the container element
    var navbarContainer = document.getElementById('navbarContainer');

    // Create a new XMLHttpRequest object
    var xhr = new XMLHttpRequest();

    // Configure it: GET-request for the navbar.html file
    xhr.open('GET', 'navbar.html', true);

    // Define the onload handler
    xhr.onload = function () {
        if (xhr.status === 200) {
            // Insert the HTML content into the container
            navbarContainer.innerHTML = xhr.responseText;
        }
    };

    // Send the request
    xhr.send();
});
