import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average"
# url = 'https://bullishbears.com/dow-jones-stocks-list/'
response = requests.get(url)
print(response)

if response.status_code ==200:
    print("It's working")


# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the stock data (The table with id 'constituents')
table = soup.find("table", {"id": "constituents"})
print(table)
