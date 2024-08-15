import os

# Directory containing the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Directory containing the images
image_folder = script_directory

# Output HTML file with the name of the parent directory
output_file = f"{os.path.basename(script_directory)}.html"

# Get a list of image files in the folder
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

# Generate HTML code
html_code = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Slideshow with Textbox</title>

  <style>
    * {{
      box-sizing: border-box;
    }}

    /* Slideshow container */
    .slideshow-container {{
      max-width: max-content; /* ensure images don't get stretched */
      position: relative;
      margin: auto;
    }}

    /* Hide the images by default */
    .mySlides {{
      display: none;
    }}

    /* Next & previous buttons */
    .prev, .next {{
      cursor: pointer;
      position: absolute;
      top: 50%;
      width: auto;
      margin-top: -22px;
      padding: 16px;
      color: white;
      font-weight: bold;
      font-size: 24px;
      transition: 0.6s ease;
      border-radius: 0 3px 3px 0;
      user-select: none;
      background-color: rgba(0, 0, 0, 0.8);
    }}

    /* Position the "next button" to the right */
    .next {{
      right: 0;
      border-radius: 3px 0 0 3px;
    }}

    /* On hover, add a black background color with a little bit see-through */
    .prev:hover, .next:hover {{
      background-color: #333;
    }}

    /* Number text (1/3 etc) */
    .numbertext {{
      color: #f2f2f2;
      font-size: 12px;
      padding: 8px 12px;
      position: absolute;
      top: 0;
    }}

    /* The dots/bullets/indicators */
    .dot {{
      height: 15px;
      width: 15px;
      margin: 0 2px;
      background-color: #bbb;
      border-radius: 50%;
      display: inline-block;
      transition: background-color 0.6s ease;
    }}

    .active, .dot:hover {{
      background-color: #717171;
    }}

    /* Fading animation */
    .fade {{
      animation-name: fade;
      animation-duration: 1.5s;
    }}

    @keyframes fade {{
      from {{opacity: .4}}
      to {{opacity: 1}}
    }}

    /* Additional styles for the copy button */
    .copy-button {{
      margin-top: 10px;
      cursor: pointer;
      background-color: #4CAF50;
      color: white;
      border: none;
      padding: 10px 20px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      border-radius: 5px;
    }}

    .copy-button:hover {{
      background-color: #45a049;
    }}

    /* Additional styles for the code box */
    .code-section {{
      text-align: center;
      margin-top: 10px;
    }}

    .code-section textarea {{
      width: 100%;
      box-sizing: border-box;
    }}

    /* Additional styles for the plain text box */
    .text-section {{
      text-align: center;
      margin-top: 10px;
    }}

    .text-section textarea {{
      width: 100%;
      box-sizing: border-box;
    }}
  </style>
</head>
<body>

  <!-- Slideshow container -->
  <div class="slideshow-container">
"""

for i, image_file in enumerate(image_files, start=1):
    relative_image_path = os.path.relpath(os.path.join(image_folder, image_file), script_directory)
    html_code += f"""
    <!-- Full-width images with text box, code box, and copy code button -->
<div class="mySlides fade">
  <div class="numbertext">{i} / {len(image_files)}</div>
  <!-- Wrap the image in an anchor tag with a target attribute -->
  <a href="{relative_image_path}" target="_blank">
    <img src="{relative_image_path}" style="width:100%">
  </a>
  <div class="text-section">
    <p>
      Step {i}
    </p>
  </div>
<div class="code-section">
    <textarea rows="4" class="textbox code">

    </textarea>
    <button class="copy-button" onclick="copyCode({i})">Copy Code</button>
  </div>
</div>
"""

html_code += """
    <!-- Other slides here -->

    <!-- Next and previous buttons -->
    <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
    <a class="next" onclick="plusSlides(1)">&#10095;</a>
  </div>
  <br>
  
  <!-- The dots/circles -->
  <div style="text-align:center">
    <!-- Dots here -->
  </div>

  <script>
  let slideIndex = 1;
  showSlides(slideIndex);

  function plusSlides(n) {
    showSlides(slideIndex += n);
  }

  function currentSlide(n) {
    showSlides(slideIndex = n);
  }

  function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");
    let codeBoxes = document.getElementsByClassName("code-section");

    if (n > slides.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = slides.length }

    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
      if (codeBoxes[i]) {
        codeBoxes[i].style.display = "none";
      }
    }

    for (i = 0; dots && i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
    }

    if (dots && dots[slideIndex - 1]) {
      dots[slideIndex - 1].className += " active";
    }

    if (slides[slideIndex - 1]) {
      slides[slideIndex - 1].style.display = "block";
      if (codeBoxes[slideIndex - 1] && codeBoxes[slideIndex - 1].querySelector('textarea').value.trim() !== "") {
        codeBoxes[slideIndex - 1].style.display = "block";
      }
    }
  }

  // Function to copy code to clipboard
  function copyCode(slideNumber) {
    let codeTextarea = document.querySelectorAll('.code-section textarea')[slideNumber - 1];
    let codeContent = codeTextarea.value.trim();

    if (codeContent !== "") {
      navigator.clipboard.writeText(codeContent).then(function() {
        alert('Code copied to clipboard!');
      }).catch(function(err) {
        console.error('Unable to copy to clipboard', err);
      });
    }
  }
</script>

</body>
</html>
"""

# Write the HTML code to the output file
with open(os.path.join(script_directory, output_file), "w") as f:
    f.write(html_code)

print(f"HTML code has been generated and saved to {os.path.join(script_directory, output_file)}")