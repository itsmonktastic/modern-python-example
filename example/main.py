import requests
from BeautifulSoup import BeautifulSoup

def isitchristmas():
    html = requests.get('http://isitchristmas.com/').content
    soup = BeautifulSoup(html)
    print soup.noscript.string

def isithalloween():
    html = requests.get('http://isithalloween.com/').content
    soup = BeautifulSoup(html)
    print soup.h1.string
