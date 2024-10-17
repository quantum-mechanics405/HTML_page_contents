import pandas as pd
import yfinance as yf
import numpy as np
import yfinance as yf
from scipy.optimize import minimize
import ast
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

# Wikipedia URL containing Dow Jones companies list
url = "https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average"

# Send a request to fetch the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print("Failed to retrieve the page")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the stock data (The table with id 'constituents')
table = soup.find("table", {"id": "constituents"})

# Extract the rows of the table (skip the header row)
rows = table.find_all("tr")[1:]

# Initialize a list to store the data
data = []

# Loop through each row and extract the relevant columns (Symbol, Company Name, Exchange, Industry)
for row in rows:
    columns = row.find_all("td")
    symbol = columns[1].text.strip()    # Symbol (2nd column)
    name = columns[0].text.strip()      # Company Name (1st column)
    exchange = columns[2].text.strip()  # Exchange (3rd column)
    industry = columns[3].text.strip()  # Industry (4th column)
    data.append([symbol, name, exchange, industry])

# Convert the list into a DataFrame for better analysis
df = pd.DataFrame(data, columns=["Symbol", "Exchange", "Industry","Date Added"])

# Print the DataFrame
print(df)

# Save the DataFrame to CSV if needed
df.to_csv("dow_jones_companies.csv", index=False)
print(df.head(3))

