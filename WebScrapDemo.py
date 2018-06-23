# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 20:18:20 2017

@author: BALASUBRAMANIAM
"""
import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError

from urllib.error import URLError

try:
    html = requests.get("https://www.python.org/")
except HTTPError as e:

    print(e)

except URLError:

    print("Server down or incorrect domain")

else:
    res = BeautifulSoup(html.content, "html5lib");

    if res.title is None:

        print("Tag not found")

    else:

        print(res.title)
        tags = res.findAll("h2", {"class": "widget-title"})

        for tag in tags:
            print(tag.getText())



page = requests.get("http://www.thehindu.com/")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
#finding only paragraphs
#print(soup.find_all('p'))

#finding only paragraph text
print(soup.find_all('p')[0].get_text())
#finding only paragraph class
print(soup.find_all('p', class_='hidden-xs'))
print(soup.select("div p"))

page = requests.get('http://www.fabpedigree.com/james/mathmen.htm')
html = BeautifulSoup(page.content, 'html.parser')
for i, li in enumerate(html.select('li')):
        print(i, li.text)

from datetime import datetime

quote_page = 'http://www.bloomberg.com/quote/SPGSCITR:IND'

t1 = datetime.now()

page = requests.get(quote_page)

soup = BeautifulSoup(page.content, 'html.parser')

name_store = soup.find('h1', attrs={'div': 'name'})

data_name = name_store

price_store = soup.find('div', attrs={'class': 'price'})

price = price_store.text

print (data_name)

t2 = datetime.now()

total = t2 - t1

# Collect and parse first page
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
artist_name_list = soup.find(class_='BodyText')

# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')

artist_name_list = soup.find(class_='BodyText')
artist_name_list_items = artist_name_list.find_all('a')

# Create for loop to print out all artists' names
for artist_name in artist_name_list_items:
    print(artist_name.prettify())

page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')

soup = BeautifulSoup(page.text, 'html.parser')

# Remove bottom links
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

artist_name_list = soup.find(class_='BodyText')
artist_name_list_items = artist_name_list.find_all('a')

for artist_name in artist_name_list_items:
    print(artist_name.prettify())

page = requests.get('https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm')

soup = BeautifulSoup(page.text, 'html.parser')

last_links = soup.find(class_='AlphaNav')
last_links.decompose()
import csv
# Create a file to write to, add headers row
f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

artist_name_list = soup.find(class_='BodyText')
artist_name_list_items = artist_name_list.find_all('a')

for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://web.archive.org' + artist_name.get('href')


    # Add each artist’s name and associated link to a row
    f.writerow([names, links])


'''
print('scraping completed in ', total)

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

quotes=[]  # a list to store quotes

table = soup.find('div', attrs = {'id':'container'})

for row in table.findAll('tr', attrs = {'class':'quote'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.h6.text
    quote['author'] = row.p.text
    quotes.append(quote)

filename = 'inspirational_quotes.csv'
with open(filename, 'wb') as f:
    f.write(['theme','url','img','lines','author'])
    #w.writeheader()
    for quote in quotes:
        f.writerow(quote)
'''
'''
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

print(period)
print(short_desc)
print(temp)

req = requests.get('https://en.wikipedia.org/wiki/Movies', verify=True)
soup = BeautifulSoup(req.text, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.p.contents)

'''
