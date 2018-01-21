import requests
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
        print tr.find('th').find('a').string.encode('utf-8').replace('at-large', '').replace("\xc2\xa0", '')

if __name__ == '__main__':
    with open('wiki.html') as f:
        parse_tables(f.read())
