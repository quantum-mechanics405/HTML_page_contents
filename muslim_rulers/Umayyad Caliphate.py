import requests
from bs4 import BeautifulSoup
import pandas as pd

# Wikipedia URL containing Dow Jones companies list
url = "https://en.wikipedia.org/wiki/List_of_caliphs"

# Send a request to fetch the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print("Failed to retrieve the page")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find_all('table',class_ = 'wikitable')
r = table[1].find_all('tr')
rows = r[1:]
dictionary = {'Name':[],'Born':[],'Reigned from':[],'Reigned until':[],'Relationship with predecessor':[]}
for row in rows:
    cells = row.find_all('td')
    dictionary['Name'].append(cells[1].find('b').get_text().strip())
    dictionary['Born'].append(cells[2].get_text().strip())
    reigned_text = cells[4].get_text().split('<br')[0].strip()
    dictionary['Reigned until'].append(reigned_text)
    dictionary['Reigned from'].append(cells[3].get_text().strip())
    dictionary['Relationship with predecessor'].append(cells[5].get_text().strip())


df = pd.DataFrame.from_dict(dictionary)
df.to_csv('muslim_rulers/Umayyad Caliphate.csv',index=False)
print(df.head(15))

    
# print(table)