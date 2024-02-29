import requests
import csv
from bs4 import BeautifulSoup

root = "site"
links = []
    
for link in links:
    response = requests.get(f'{root}/{link}')
    
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')

    title = soup.find('h1').get_text()
    

    with open('dump.csv', 'a', newline='',encoding="utf-8") as csvfile:
       postdump = csv.writer(csvfile, delimiter=',')
       postdump.writerow([link,title,"".join([p.text for p in soup.find_all("p")])])
            
       print(title + ' stashed')
    

