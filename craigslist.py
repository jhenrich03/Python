### This script parses the HTML from an apartments/housing Craigslist page and
### returns information such as the date it was added, a description, price, and address if listed. 

# Import the requests and BeautifulSoup modules
import requests
from bs4 import BeautifulSoup

# Input a URL from the apartments/housing Craigslist page
url = "CRAIGSLIST_URL_HERE"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

apartments = soup.find_all('p', class_='result-info')

Descriptions = []
Prices = []
Dates = []
Addresses = []
Links = []

# Loop through each apartment and pull the info we want
for a in apartments:
    descr = a.find('a', class_='result-title hdrlnk')
    link = a.find('a', class_='result-title hdrlnk').attrs['href']
    price = a.find('span', class_='result-price')
    date = a.find('time', class_='result-date')
    if not a.find('span', class_='result-hood'):
        address = 'Address Not Found'
    else:
        address = a.find('span', class_='result-hood').text.replace(' (', '').replace(')', '')
  
    Descriptions.append(descr.text)
    Prices.append(price.text)
    Dates.append(date.text)
    Addresses.append(address)
    Links.append(link)

# Print out the relevant info for each apartment found
for i in range(len(apartments)):
    print("Date added: {}\n"
          "Address: {}\n"
          "Description: {}\n"
          "Price: {}\n"
          "Link: {}\n".format(Dates[i], Addresses[i], Descriptions[i], Prices[i], Links[i]))
