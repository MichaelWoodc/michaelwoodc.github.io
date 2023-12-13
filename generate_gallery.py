def generate_gallery_html(start_number, end_number, directory):
    html_template = """
<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="{img_path}">
      <img src="{img_path}" alt="Image {img_number}">
    </a>
    <div class="desc"> Insert description here </div>
  </div>
</div>
"""

    for img_number in range(start_number, end_number + 1):
        img_path = f"{directory}\\{img_number:02d}.jpeg"
        print(html_template.format(img_number=img_number, img_path=img_path))


# Set your desired range and directory
start_number = 1
end_number = 20
image_directory = "media\\installxampp"

# Generate and print the HTML code
generate_gallery_html(start_number, end_number, image_directory)