import requests
from bs4 import BeautifulSoup
import pandas as pd

# Wikipedia URL containing Dow Jones companies list
url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

# Send a request to fetch the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print("Failed to retrieve the page")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table',class_ = 'wikitable')
r = table.find_all('tr')
rows = r[1:]
dictionary = {'Symbol':[],'Security':[],'GICS Sector':[],'GICS Sub-industry':[],'Headquarter Location':[],'Date added':[],'Founded':[]}
for row in rows:
    cells = row.find_all('td')
    dictionary['Symbol'].append(cells[0].get_text().strip())
    dictionary['Security'].append(cells[1].get_text().strip())
    dictionary['GICS Sector'].append(cells[2].get_text().strip())
    dictionary['GICS Sub-industry'].append(cells[3].get_text().strip())
    dictionary['Headquarter Location'].append(cells[4].get_text().strip())
    dictionary['Date added'].append(cells[5].get_text().strip())
    dictionary['Founded'].append(cells[-1].get_text().strip())


df = pd.DataFrame.from_dict(dictionary)
df.to_csv('S&P_500_companies/S&P500 Companies.csv',index=False)
print(df.head(200))
print(df.iloc[-1, -1])
    
# print(table)