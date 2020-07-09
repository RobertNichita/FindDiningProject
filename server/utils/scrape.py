# python module to scrape data from website
from bs4 import BeautifulSoup
from requests import get
import time
import csv


def scrape_wiki():
    # sources of data
    # url = 'https://en.wikipedia.org/wiki/List_of_Asian_cuisines'
    # url = 'https://en.wikipedia.org/wiki/List_of_African_cuisines'
    # url = 'https://en.wikipedia.org/wiki/List_of_cuisines_of_the_Americas'
    # url = 'https://en.wikipedia.org/wiki/List_of_European_cuisines'
    # url = 'https://en.wikipedia.org/wiki/Oceanic_cuisine'

    urls = [
        'https://en.wikipedia.org/wiki/List_of_Asian_cuisines',
        'https://en.wikipedia.org/wiki/List_of_African_cuisines',
        'https://en.wikipedia.org/wiki/List_of_cuisines_of_the_Americas',
        'https://en.wikipedia.org/wiki/List_of_European_cuisines',
        'https://en.wikipedia.org/wiki/Oceanic_cuisine'
    ]

    start = time.time()
    s = set()
    for url in urls:
        response = get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            if 'cuisine' in link.text and link.text.count(' ') < 2 and link.text.replace(' ', '').isalpha():
                s.add(link.text.replace('cuisines', '').replace('cuisine', ''))

    l = [elem for elem in s]
    lmat = [l[i:i + 3] for i in range(0, len(l), 3)]
    write(lmat, 'cuisine.csv')

    end = time.time()
    print(str(len(s)) + ' items loaded in ' + str((end - start)) + ' s')


def scrape_dish():
    start = time.time()
    # source = https://theodora.com/food/culinary_dictionary_food_glossary_.html

    urls = ['https://theodora.com/food/index.html']  # a does not fit pattern
    for i in range(98, 98 + 25):
        req = 'https://theodora.com/food/culinary_dictionary_food_glossary_' + chr(i) + '.html'
        urls.append(req)
    s = set()
    # parse html
    for url in urls:
        parser = BeautifulSoup(get(url).text, 'html.parser')
        for term in parser.find_all('b'):
            if ':' in term.text and term.text.count(' ') == 0:
                s.add(term.text.replace(':', '').replace('\t', ''))

    l = [elem for elem in s]
    lmat = [l[i:i + 3] for i in range(0, len(l), 3)]
    write(lmat, '../cuisine_dict/dishes.csv')

    end = time.time()

    print('loaded ' + str(len(s)) + ' elements ' + str((end - start)) + ' s')


def write(data , file_name):
    f = open(file_name, 'w')

    with f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
