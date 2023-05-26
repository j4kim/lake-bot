from bs4 import BeautifulSoup
import requests

url = "https://www.bateau24.ch/chfr/service/temperaturen/lacdeneuchatel/"
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

print(soup.title)