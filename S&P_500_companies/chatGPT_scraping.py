import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Get the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the first table in the page
table = soup.find('table', {'id': 'constituents'})

# Read the table into a DataFrame
df = pd.read_html(str(table))[0]

# Display the DataFrame
print(df.head(200))
