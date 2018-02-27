import requests
from bs4 import BeautifulSoup

url = "https://milwaukee.craigslist.org/search/apa?hasPic=1&postedToday=1&bundleDuplicates=1&min_price=0&max_price=1500&min_bedrooms=1&availabilityMode=2&sale_date=all+dates"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

apartments = soup.find_all('p', class_='result-info')

Descriptions = []
Prices = []
Dates = []
Addresses = []
Links = []


for a in apartments:
    descr = a.find('a', class_='result-title hdrlnk')
    link = a.find('a', class_='result-title hdrlnk').attrs['href']
    price = a.find('span', class_='result-price')
    date = a.find('time', class_='result-date')
    if not a.find('span', class_='result-hood'):
        address = 'Milwaukee, WI'
    else:
        address = a.find('span', class_='result-hood').text.replace(' (', '').replace(')', '')

    Descriptions.append(descr.text)
    Prices.append(price.text)
    Dates.append(date.text)
    Addresses.append(address)
    Links.append(link)


for i in range(len(apartments)):
    print("Date added: {}\n"
          "Address: {}\n"
          "Description: {}\n"
          "Price: {}\n"
          "Link: {}\n".format(Dates[i], Addresses[i], Descriptions[i], Prices[i], Links[i]))







