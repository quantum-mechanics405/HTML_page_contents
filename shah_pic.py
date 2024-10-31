from bs4 import BeautifulSoup
import requests
import os
from urllib.parse import urljoin

# URL of the page containing the image
page_url = 'https://www.google.com/search?sca_esv=7a9852a0e09aadea&rlz=1C1NDCM_enPK1046PK1046&sxsrf=ADLYWILsnBuzxoNmWd1xSqpBT3MGij0WGg:1730379951086&q=shahrukh+khan&udm=2&fbs=AEQNm0Aa4sjWe7Rqy32pFwRj0UkWd8nbOJfsBGGB5IQQO6L3J5MIFhvnvU242yFxzEEp3BcbXWGQjBp6XyyqfUu6Wz8hWk3bMeDVtqu_mrB1o-K4YflJcFQPwF_8HcO4g0e23yGFHocWKhGHUVyRw0szLJnh8A9Sf22qKDz0aW7pjYIFVMMH0Lk&sa=X&ved=2ahUKEwi3g77S17iJAxUGB9sEHU5RHyMQtKgLegQIFxAB'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Send a request to get the HTML content of the page
response = requests.get(page_url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the specific image using the src partial match or class name
# Option 1: Find by partial 'src' match (using a part of the URL)
img_all = soup.find('div', jscontroller = 'gOTY1')
# print(img_all)
# Option 2: Find by class name (if class name is unique)
# img_tag = soup.find('img', class_="mw-file-element")
i=0
for img_ta in img_all.find_all('h3',class_ = "ob5Hkd"):
    img_tag = img_ta.find('img') 
# Get the src attribute of the image
    i=i+1
    if img_tag:
        relative_image_url = img_tag['src']
        
        # Complete the image URL by adding the "https:" protocol
        image_url = urljoin('https:', relative_image_url)

        # Create a folder to save the image
        os.makedirs('shah Rukh Khan Images', exist_ok=True)

        # Download the image
        img_response = requests.get(image_url)

        # Save the image
        if img_response.status_code == 200:
            image_name = f"Shah Rukh Khan{i}.jpg"
            image_path = os.path.join('downloaded_image', image_name)
            with open(image_path, 'wb') as f:
                f.write(img_response.content)
            print(f"Image downloaded successfully: {image_path}")
        else:
            print(f"Failed to download the image. Status code: {img_response.status_code}")
    else:
        print("Image not found.")
