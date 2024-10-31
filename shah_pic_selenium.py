from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import requests
import time
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the Google Images search page
page_url = 'https://www.google.com/search?q=shahrukh+khan&tbm=isch'
driver.get(page_url)

# Wait for the page to load
time.sleep(5)  # You may adjust the sleep time based on internet speed

# Create a folder to save the images
os.makedirs('ShahRukhKhanImages', exist_ok=True)

# Locate image elements on the page
images = driver.find_elements(By.CSS_SELECTOR, "img.rg_i")

# Loop through images and download them
for i, img in enumerate(images[:10]):  # Limiting to first 10 images for example
    try:
        # Attempt to get the image URL from 'src' or 'data-src'
        img_url = img.get_attribute("src") or img.get_attribute("data-src")
        if img_url and img_url.startswith("http"):
            # Send a request to download the image
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                # Save the image
                image_path = os.path.join('ShahRukhKhanImages', f'ShahrukhKhan_{i+1}.jpg')
                with open(image_path, 'wb') as f:
                    f.write(img_response.content)
                print(f"Image downloaded successfully: {image_path}")
            else:
                print(f"Failed to download image {i+1}. Status code: {img_response.status_code}")
        else:
            print(f"No valid URL for image {i+1}")
    except Exception as e:
        print(f"Error downloading image {i+1}: {e}")

# Close the WebDriver
driver.quit()
