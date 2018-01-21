import re
from bs4 import BeautifulSoup


def parse_tables(content):
    soup = BeautifulSoup(content, 'lxml')
    print('bs parsed')
    table_classes = {"class": ["sortable", "wikitable"]}
    wikitables = soup.findAll("table", table_classes)

    for table in wikitables[:-1]:
        analyze_table(table)

def analyze_table(table):
    info = {}
    for tr in table.findAll('tr')[2:]:
        code = tr.find('th').find('a').string.encode('utf-8').replace('at-large', '').replace("\xc2\xa0", '')
        results = str(tr.findAll('td')[-1])
        rep = results[results.find('(Republican)') + 13:results.find('(Republican)') + 17]
        dem = results[results.find('(Democratic)') + 13:results.find('(Democratic)') + 17]
        print rep, dem

if __name__ == '__main__':
    with open('wiki.html') as f:
        parse_tables(f.read())
