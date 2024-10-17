import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the webpage you want to scrape
url = 'https://en.wikipedia.org/wiki/Joseph_Stalin'

# Send a request to fetch the HTML content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    html_content = response.text  # Get the HTML content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the img tags in the page
    images = soup.find_all('img')

    # Create a folder to save the images
    os.makedirs('downloaded_images', exist_ok=True)

    # Download each image
    for i, img in enumerate(images):
        # Get the image source (src)
        img_url = img.get('src')

        # Ensure the image URL is complete (handles relative URLs)
        img_url = urljoin(url, img_url)

        # Send a request to download the image
        img_response = requests.get(img_url)

        # Save the image
        if img_response.status_code == 200:
            img_name = f"image_{i+1}.jpg"
            img_path = os.path.join('downloaded_images', img_name)
            with open(img_path, 'wb') as f:
                f.write(img_response.content)
            print(f"Downloaded: {img_name}")
        else:
            print(f"Failed to download image from: {img_url}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
