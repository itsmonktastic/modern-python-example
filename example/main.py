import requests
from BeautifulSoup import BeautifulSoup

def is_it_christmas():
    html = requests.get('http://isitchristmas.com/').content
    soup = BeautifulSoup(html)
    print soup.noscript.string

def is_it_halloween():
    html = requests.get('http://isithalloween.com/').content
    soup = BeautifulSoup(html)
    print soup.h1.string
