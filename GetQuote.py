import lxml
import urllib.request
from bs4 import BeautifulSoup
import re
import os
import random

url = "http://www.quotationspage.com/random.php"
request = urllib.request.Request(url)
html = urllib.request.urlopen(request)
soup = BeautifulSoup(html, 'lxml')
links = soup.findAll('a', {"title":"Click for further information about this quotation"})
quotes=[]
for a in links:
    quotes.append(str(a)[str(a).find('>')+1:str(a).rfind('<')])

quote = random.choice(quotes)
with open("C:\\Users\\Arthur Mayer\\OneDrive\\Documents\\HackCU_V\\randomQuote.txt", "w") as outFile:
    outFile.write(quote)
    outFile.close()
