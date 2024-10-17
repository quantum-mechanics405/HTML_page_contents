from bs4 import BeautifulSoup
import requests
import os
from urllib.parse import urljoin

# URL of the page containing the image
page_url = 'https://en.wikipedia.org/wiki/Adolf_Hitler'

# Send a request to get the HTML content of the page
response = requests.get(page_url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the specific image using the src partial match or class name
# Option 1: Find by partial 'src' match (using a part of the URL)
img_tag = soup.find('img', {'src': lambda x: x and 'Adolf_Hitler_und_Eva_Braun' in x})

# Option 2: Find by class name (if class name is unique)
# img_tag = soup.find('img', class_="mw-file-element")

# Get the src attribute of the image
if img_tag:
    relative_image_url = img_tag['src']
    
    # Complete the image URL by adding the "https:" protocol
    image_url = urljoin('https:', relative_image_url)

    # Create a folder to save the image
    os.makedirs('downloaded_image', exist_ok=True)

    # Download the image
    img_response = requests.get(image_url)

    # Save the image
    if img_response.status_code == 200:
        image_name = "Adolf_Hitler_and_Eva_Braun.jpg"
        image_path = os.path.join('downloaded_image', image_name)
        with open(image_path, 'wb') as f:
            f.write(img_response.content)
        print(f"Image downloaded successfully: {image_path}")
    else:
        print(f"Failed to download the image. Status code: {img_response.status_code}")
else:
    print("Image not found.")
