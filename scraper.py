"""Scrape temperature data from bateau24.ch"""

from bs4 import BeautifulSoup
import requests

URL = "https://www.bateau24.ch/chfr/service/temperaturen/lacdeneuchatel/"

def scrape():
    """Make a request to the website and parse the data"""

    html = requests.get(URL, timeout=10).text

    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("h2", string="Lac de neuchâtel")
    lis = title.parent.ul.find_all("li")

    data = [{
        "temperature": int(li.span.text[:-1]),
        "day": li.p.text
    } for li in lis]

    return data
