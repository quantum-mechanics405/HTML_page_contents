import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://en.wikipedia.org/wiki/Joseph_Stalin'

# Send a request to fetch the HTML content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    html_content = response.text  # Get the HTML content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Example: Get all the headings (h1) from the page
    headings = soup.find_all('h1')

    # Print the headings
    for heading in headings:
        print(heading.text)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
