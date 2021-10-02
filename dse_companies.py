from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.dsebd.org/company_listing.php'

page = requests.get(url)
# print(page)
soup = BeautifulSoup(page.content, 'html.parser')
companies = soup.find_all('div', class_="BodyContent")

# 'div', class_='col-lg-4 col-md-4 col-sm-6 col-xs-12 background-white')  # find('div', class_="BodyContent").find('a', class_='ab1').text

l = []
for company in companies:
    classes = company.find_all('a', class_='ab1')
    for c in classes:
        # print(c.text)
        l.append(c.text)


print(len(l))
for idx, i in enumerate(l):
    print(idx+1, " ", i)
