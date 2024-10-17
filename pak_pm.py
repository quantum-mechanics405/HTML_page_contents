import pandas as pd
import requests
from bs4 import BeautifulSoup

# Wikipedia URL containing the list of Prime Ministers of Pakistan
url = "https://en.wikipedia.org/wiki/List_of_prime_ministers_of_Pakistan"

# Send a request to fetch the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print("Failed to retrieve the page")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Try to find the first table with the class 'wikitable'
table = soup.find("table", {"class": "wikitable"})

# Check if the table was found
if table is None:
    print("Failed to find the table")
    exit()

# Initialize a list to store rows
rows = []

# Loop through the rows of the table
for tr in table.find_all('tr')[1:]:  # Skip the header row
    tds = tr.find_all('td')
    if len(tds) >= 5:  # Ensure there are enough columns
        name = tds[0].get_text(strip=True)
        took_office = tds[1].get_text(strip=True)
        left_office = tds[2].get_text(strip=True)
        tenure = tds[3].get_text(strip=True)
        political_party = tds[4].get_text(strip=True)
        
        # Append a tuple of the extracted data
        rows.append([name, took_office, left_office, tenure, political_party])

# Create a DataFrame with the extracted data
df = pd.DataFrame(rows, columns=['Name', 'Took office', 'Left office', 'Tenure', 'Political party'])
print(df.head(5))
# # Save the DataFrame to a CSV file
# output_file = 'prime_ministers_of_pakistan.csv'
# df.to_csv(output_file, index=False)

# print(f"Data saved to {output_file}")
