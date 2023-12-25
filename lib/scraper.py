from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)
doc = BeautifulSoup(html.text, 'html.parser')
h4s = doc.select('.heading-25-semibold.color-white')
for h4 in h4s:
    print(h4.contents[0].strip())