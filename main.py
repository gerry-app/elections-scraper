import requests
from bs4 import BeautifulSoup

WIKI_URL = "https://en.wikipedia.org/wiki/United_States_House_of_Representatives_elections,_2016"

req = requests.get(WIKI_URL)
content = req.content[req.content.find('<span class="mw-headline" id="Complete_list_of_elections">Complete list of elections</span>'):]
soup = BeautifulSoup(content, 'lxml')
table_classes = {"class": ["sortable", "wikitable"]}
wikitables = soup.findAll("table", table_classes)

print len(wikitables)
print wikitables[0]
