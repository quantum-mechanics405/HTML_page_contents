import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

# API endpoint
url = "https://api.thedogapi.com/v1/images/search?limit=5"

# Make the request to fetch 5 random dog images
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    dog_images = response.json()  # Get the list of image URLs
    # Set up a plot grid to display images
    plt.figure(figsize=(15, 5))  # Adjust the size of the plot grid
    num_images = len(dog_images)  # Number of images returned by the API

    for i, dog in enumerate(dog_images):
        img_url = dog['url']
        img_response = requests.get(img_url)  # Fetch the image
        img = Image.open(BytesIO(img_response.content))  # Open image from bytes

        # Display image in a subplot (1 row, 5 columns)
        plt.subplot(1, num_images, i + 1)  # Use the correct number of subplots dynamically
        plt.imshow(img)
        plt.axis('off')  # Hide axes for a cleaner look
    
    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()
else:
    print(f"Failed to fetch images, status code: {response.status_code}")
