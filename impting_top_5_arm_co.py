import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of SIPRI page containing the top 100 arms-producing companies
url = "https://www.sipri.org/visualizations/2023/sipri-top-100-arms-producing-and-military-services-companies-world-2022"

# Send a request to fetch the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print("Failed to retrieve the page")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the first table in the page
table = soup.find('table', {'cellspacing': '0'})

# Check if table exists
if not table:
    print("No table found on the page.")
    exit()

# Find the table body and rows
tbody = table.find('tbody')
rows = tbody.find_all('tr')

# Dictionary to hold the data
dictionary = {'Name': [], 'Country': []}

# Iterate through each row and extract relevant data
for row in rows:
    cells = row.find_all('td')
    if len(cells) > 2:  # Ensure there are enough cells in the row
        company_name = cells[1].get_text().strip()  # Company name
        country = cells[2].get_text().strip()  # Country name
        dictionary['Name'].append(company_name)
        dictionary['Country'].append(country)

# Convert dictionary to pandas DataFrame
df = pd.DataFrame(dictionary)

# Print first 10 entries and last cell for testing
print(df.head(10))
print(df.iloc[-1, -1])
