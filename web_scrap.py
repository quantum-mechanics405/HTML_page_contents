import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetchandDownload(url, path):
    r = requests.get(url)
    with open(path,'w', encoding='utf-8') as f:
        f.write(r.text)

url = 'https://en.wikipedia.org/wiki/Marco_Polo'

fetchandDownload(url,'MarcoPolo/wikipedia.html')