import os
import requests
from urllib.parse import urljoin

# URL of the webpage where the image is found
base_url = "https://en.wikipedia.org/wiki/Adolf_Hitler"

# Relative image URL (from the src attribute of the img tag)
relative_image_url = "//upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Hitler_portrait_crop.jpg/220px-Hitler_portrait_crop.jpg"

# Complete the image URL by adding the "https:" protocol
image_url = urljoin("https:", relative_image_url)

# Create a folder to save the image
os.makedirs('downloaded_image', exist_ok=True)

# Send request to download the image
response = requests.get(image_url)

# Save the image
if response.status_code == 200:
    image_name = "portrait_of_hitler.jpg"
    image_path = os.path.join('downloaded_image', image_name)
    with open(image_path, 'wb') as f:
        f.write(response.content)
    print(f"Image downloaded successfully: {image_path}")
else:
    print(f"Failed to download the image. Status code: {response.status_code}")
