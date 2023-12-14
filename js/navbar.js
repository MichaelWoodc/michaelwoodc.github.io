document.addEventListener('DOMContentLoaded', function () {
    // Get the container element
    var navbarContainer = document.getElementById('navbarContainer');

    // Create a new XMLHttpRequest object
    var xhr = new XMLHttpRequest();

    // Configure it: GET-request for the navbar.html file
    xhr.open('GET', '../navbar.html', true); // Update the path here

    // Define the onload handler
    xhr.onload = function () {
        if (xhr.status === 200) {
            // Insert the HTML content into the container
            navbarContainer.innerHTML = xhr.responseText;

            // Fix the links in the navbar
            fixNavbarLinks();
        }
    };

    // Send the request
    xhr.send();

    // Add click event listeners to the copy buttons
    document.querySelectorAll('.copy-button').forEach(button => {
        button.addEventListener('click', copyCode);
    });
});

// Function to copy code to clipboard
function copyCode(event) {
    const codeText = event.target.previousElementSibling.textContent;
    const tempTextArea = document.createElement('textarea');
    tempTextArea.value = codeText;
    document.body.appendChild(tempTextArea);
    tempTextArea.select();
    document.execCommand('copy');
    document.body.removeChild(tempTextArea);
    alert('Code has been copied to clipboard');
}

// Function to fix navbar links
function fixNavbarLinks() {
    const navbarLinks = document.querySelectorAll('.navbar a');
    navbarLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href && !href.startsWith('http')) {
            // Update relative paths dynamically based on the current page's location
            link.href = '../' + href;
        }
    });
}
