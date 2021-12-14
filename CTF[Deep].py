import requests
from bs4 import BeautifulSoup


url = 'http://139.59.156.24:1945/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

for hit in soup.findAll(attrs={'class': 'youCantSeeMe'}):
    # print(hit) => <p class="youCantSeeMe">WQ8RLQ3.html</p>
    url += hit.text 
    print(url) # http://139.59.156.24:1945/WQ8RLQ3.html
    
x=1
while (x == 1):
    # url = http://139.59.156.24:1945/WQ8RLQ3.html
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    for hit in soup.findAll(attrs={'class': 'youCantSeeMe'}):
        url = url[0:26:] # http://139.59.156.24:1945/
        url += hit.text  # http://139.59.156.24:1945/ + hit.text
        print(url)
    
    
        
    


