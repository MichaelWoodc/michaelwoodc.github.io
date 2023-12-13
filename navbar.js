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

// Function to copy code to clipboard
function copyCode(event) {
    const codeBlock = event.target.previousElementSibling;
    const codeText = codeBlock.textContent || codeBlock.innerText;
    const tempTextArea = document.createElement('textarea');
    tempTextArea.value = codeText;
    document.body.appendChild(tempTextArea);
    tempTextArea.select();
    document.execCommand('copy');
    document.body.removeChild(tempTextArea);
    alert('Code has been copied to clipboard');
}
// Add click event listeners to the copy buttons
const copyButtons = document.querySelectorAll('.copy-button');
copyButtons.forEach(button => {
    button.addEventListener('click', copyCode);
});
