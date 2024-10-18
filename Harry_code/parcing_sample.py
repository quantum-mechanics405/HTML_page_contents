import requests
from bs4 import BeautifulSoup

with open('Harry_code\sample.html', 'r') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc,'html.parser')

a = soup.title.string                               #fetching the title as string         ouotput DSample Code
# print(a[0])                                         #printing first element of the string   D
# print(soup.title)                                   #<title>DSample Code</title>
# print(soup.h2)                                      #print(soup.h2) 
# print(soup.prettify())                            #prettifying and printing the code
# print(soup.find("h1"))                              #<h1 class="header">This is my sample code</h1>
# print(soup.find("h2",class_ = 'header2').contents)  #['Muhammad Umar']
# print(soup.button.text)                             #search
#find all give all such things which match its argument as LIST (important)
# print(soup.find_all('h1'))                          #[<h1 class="header">This is my sample code</h1>, <h1 class="header3">Good code</h1>]

# printing all links
for link in soup.find_all("a"):
    print(link)                                       #getting all links
    print(link.get("href"))                           #for just getting link