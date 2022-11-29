from bs4 import BeautifulSoup
import requests, re

data = requests.get("https://www.sharmusic.com/Tchaikovsky-Concerto-In-D-Violin-Piano-Urtext?quantity=1").content
soup = BeautifulSoup(data, 'html.parser')
span = soup.find("h1", {"class":"product_information_title___2eG9< product_title gl-heading gl-heading--m"})
title = span.text
span = soup.find("span", {"class":"gl-price__value gl-price__value--sale"})
price = span.text
print("Item %s is this price %s" % (title, price))