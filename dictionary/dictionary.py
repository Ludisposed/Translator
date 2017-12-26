from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import sys

BASE_URL = "https://www.ldoceonline.com/dictionary/"

def get_soup(url):
    return BeautifulSoup(urlopen(url).read(), "html.parser")

def parse(word, soup):
    if "Did you mean:" in soup.text:
        return [], ""

    meanings = []
    for s in soup.find_all(id=re.compile("{}__".format(word))):
        if s.find('span', class_='DEF'):
            meanings.append(s.find('span', class_='DEF').text)
    prounce = soup.find('span',class_='PRON').string

    return meanings, prounce

def presentation(word, meanings, prounce):
    print('{}: {}'.format(word, prounce))
    for idx, meaning in enumerate(meanings):
        print('{}: {}'.format(idx, meaning))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage python dictionary.py [word]")
        exit(0)
    word = sys.argv[1]
    meanings, prounce = parse(word,get_soup(BASE_URL + word))
    presentation(word, meanings, prounce)
