import pandas as pd
import requests
from bs4 import BeautifulSoup

# Wikipedia URL
url = "https://en.wikipedia.org/wiki/List_of_caliphs"

# Send a request to fetch the page content
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the first table on the page
table = soup.find('table', {'class': 'wikitable'})

# Extract headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract table rows
rows = []
for tr in table.find_all('tr')[1:]:  # Skip the header row
    data = [td.text.strip() for td in tr.find_all('td')]
    if data:
        rows.append(data)

# Create DataFrame
df = pd.DataFrame(rows, columns=headers)

# Display DataFrame
print(df)
