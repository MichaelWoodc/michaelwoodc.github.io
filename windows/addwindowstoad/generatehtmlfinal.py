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

"""

# Write the HTML code to the output file
with open(os.path.join(script_directory, output_file), "w") as f:
    f.write(html_code)

print(f"HTML code has been generated and saved to {os.path.join(script_directory, output_file)}")