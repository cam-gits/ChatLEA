import requests
from bs4 import BeautifulSoup

root = "site"
links = []
stash = open("dump.txt", "a") 

for link in links:
    response = requests.get(f'{root}/{link}')
    
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')

    title = soup.find('title').get_text()
    paragraphs = "".join([p.text for p in soup.find_all("p")])
    try:
        stash.write("".join([p.text for p in soup.find_all("p")]))
        print(title + ' stashed')
    except:
        print('Error in: ' + title)
        print(paragraphs)
    
stash.close()

