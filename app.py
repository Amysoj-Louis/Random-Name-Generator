import requests
from bs4 import BeautifulSoup

url = 'https://www.behindthename.com/random/random.php?number=2&sets=1&gender=both&surname=&usage_ind=1'
First_name = ''
last_name = ''
r = requests.get(url)
data = r.content
soup = BeautifulSoup(data, "html.parser")
for link in soup.findAll('a'):
    rawlink = link.get('href')
    if ("/name/" in rawlink):
        if (First_name == ''):
            First_name = rawlink.split("/")[2]
        else:
            last_name = rawlink.split("/")[2]
name = f'{First_name.capitalize()} {last_name.capitalize()}'
print(f'Name: {name}')
