# pip install beautifulsoup4
# pip install lxml
# pip install requests

from bs4 import BeautifulSoup
import requests
import time


def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    idx = 0
    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            idx += 1
            comp_name = job.find('h3', class_='joblist-comp-name').text
            skills = job.find(
                'span', class_='srp-skills').text.replace(' ,', ',')
            more_info = job.header.h2.a['href']
            print(f'Job no. {idx}')
            print(f'Comapany name: {comp_name.strip()}')
            print(f'Required Skills: {skills.strip()}')
            print(f'More info: {more_info}')
            print('------------------------------------------------')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 0.5
        print(f'Waiting {time_wait} minutes...........')
        time.sleep(time_wait*60)
