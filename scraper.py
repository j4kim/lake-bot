"""Scrape temperature data from bateau24.ch"""

from bs4 import BeautifulSoup
import requests
import config

def scrape():
    """Make a request to the website and parse the data"""

    html = requests.get(config.URL, timeout=10).text

    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("h2", string=config.LAKE)
    lis = title.parent.ul.find_all("li")

    data = []
    for li in lis:
        t = li.span.text[:-1]
        temperature = int(t) if t.isdigit() else None
        data.append({ "temperature": temperature, "day": li.p.text })

    return data
