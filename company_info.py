from bs4 import BeautifulSoup
import requests
import time


url = 'https://www.dsebd.org/displayCompany.php?name=AAMRANET'

page = requests.get(url)
# print(page)

soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find('div', class_='row')

info = content.find('tr', class_='alt').text.strip().split('\n')

trading_code = info[0]
scrip_code = info[1]
print(trading_code, ' ', scrip_code)
