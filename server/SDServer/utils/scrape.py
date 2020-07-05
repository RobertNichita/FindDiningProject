# python module to scrape data from website
from bs4 import BeautifulSoup
from requests import get
import time


def scrape_wiki():
    # sources of data
    url = 'https://en.wikipedia.org/wiki/List_of_Asian_cuisines'
    # url = 'https://en.wikipedia.org/wiki/List_of_African_cuisines'
    # url = 'https://en.wikipedia.org/wiki/List_of_cuisines_of_the_Americas'
    # url = 'https://en.wikipedia.org/wiki/List_of_European_cuisines'
    # url = 'https://en.wikipedia.org/wiki/Oceanic_cuisine'

    start = time.time()
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    s = set()
    for link in soup.find_all('a'):
        if 'cuisine' in link.text and link.text.count(' ') < 2 and link.text.replace(' ', '').isalpha():
            s.add(link.text.replace('cuisines', '').replace('cuisine', ''))

    for elem in s:
        print(elem)

    end = time.time()
    print(str(len(s)) + ' items loaded in ' + str((end - start)) + ' s')


def scrape_dish():
    start = time.time()
    # source = https://theodora.com/food/culinary_dictionary_food_glossary_.html

    d = {'a': get('https://theodora.com/food/index.html')}  # a does not fit pattern
    for i in range(98, 98 + 25):
        req = 'https://theodora.com/food/culinary_dictionary_food_glossary_' + chr(i) + '.html'
        d[chr(i)] = get(req)

    count = 0
    # parse html
    for index in d:
        parser = BeautifulSoup(d[index].text, 'html.parser')
        d[index] = []
        for term in parser.find_all('b'):
            if ':' in term.text and term.text.count(' ') == 0:
                d[index].append(term.text.replace(':', '').replace('\t', ''))
        print('loaded ' + str(len(d[index])) + ' elements')
        count += len(d[index])
    end = time.time()

    print('loaded ' + str(count) + ' elements ' + str((end - start)) + ' s')

    return d


def list_all(d):
    for key in d:
        print('***************************************' + key + '***************************************')
        for elem in d[key]:
            print(elem)

