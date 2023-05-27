from bs4 import BeautifulSoup
import requests

URL = "https://www.bateau24.ch/chfr/service/temperaturen/lacdeneuchatel/"
html = requests.get(URL, timeout=10).text

soup = BeautifulSoup(html, "html.parser")

h2 = soup.find("h2", string="Lac de neuchâtel")
lis = h2.parent.ul.find_all("li")

data = [{
    "temperature": int(li.span.text[:-1]),
    "day": li.p.text
} for li in lis]

print(data)