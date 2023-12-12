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
function copyCodeToClipboard() {
    // Get the code block element
    var codeBlock = document.getElementById("codeBlock");
    // Create a range and select the code
    var range = document.createRange();
    range.selectNode(codeBlock);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    // Execute the copy command
    document.execCommand("copy");
    // Deselect the text
    window.getSelection().removeAllRanges();
    // Update button text
    var copyButton = document.getElementById("copyButton");
    copyButton.innerText = "Code Copied!";
    setTimeout(function() {
        copyButton.innerText = "Copy Code";
    }, 2000); // Reset button text after 2 seconds
}
// Add click event listener to the copy button
document.getElementById("copyButton").addEventListener("click", copyCodeToClipboard);
