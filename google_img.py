import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import urljoin

# Set up the Chrome driver (make sure chromedriver is installed and its path is set)
driver = webdriver.Chrome()

# Google Images URL (this could be dynamic based on your search query)
search_query = "puppies"  # Replace with your own query
url = f"https://www.google.com/search?q={search_query}&source=lnms&tbm=isch"

# Open the URL
driver.get(url)

# Scroll to the bottom of the page multiple times to load more images
num_scrolls = 5
for _ in range(num_scrolls):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(2)  # Adjust if necessary to let images load

# Find all the image elements
image_elements = driver.find_elements_by_css_selector("img.rg_i")

# Limit the number of images to 50 or fewer
num_images_to_download = min(50, len(image_elements))

# Create a folder to save the images
os.makedirs('google_images', exist_ok=True)

# Download images
for i, img_element in enumerate(image_elements[:num_images_to_download]):
    try:
        img_url = img_element.get_attribute('src')

        if img_url is None:
            img_url = img_element.get_attribute('data-src')

        # Skip if the image URL is still not valid
        if not img_url:
            continue

        # Send request to download the image
        img_response = requests.get(img_url)

        # Save the image locally
        img_name = f"image_{i+1}.jpg"
        img_path = os.path.join('google_images', img_name)

        with open(img_path, 'wb') as f:
            f.write(img_response.content)

        print(f"Downloaded {img_name}")
    except Exception as e:
        print(f"Failed to download image {i+1}: {e}")

# Close the browser
driver.quit()
