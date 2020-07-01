# python module to scrape data from website
from bs4 import BeautifulSoup
from requests import get

# url = 'https://en.wikipedia.org/wiki/List_of_African_cuisines'
# url = 'https://en.wikipedia.org/wiki/List_of_cuisines_of_the_Americas'
# url = 'https://en.wikipedia.org/wiki/List_of_Asian_cuisines'
# url = 'https://en.wikipedia.org/wiki/List_of_European_cuisines'
# url = 'https://en.wikipedia.org/wiki/Oceanic_cuisine'
url = 'https://en.wikipedia.org/wiki/Fusion_cuisine'
response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')
s = set()
for link in soup.find_all('a'):
    if 'cuisine' in link.text and link.text.count(' ') < 3 and link.text.replace(' ', '').isalpha():
        s.add(link.text.replace('cuisines', '').replace('cuisine', ''))

for elem in s:
    print(elem)