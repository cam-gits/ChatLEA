import requests
from bs4 import BeautifulSoup

root = #site
links = #list 
stash = open("dump.txt", "a") 


for link in links:
    response = requests.get(f'{root}/{link}')
    
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')

    stash.write(soup.find('div', class_='content').get_text())
    print('...')

stash.close()
