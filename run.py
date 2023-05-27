"""
Description: This file runs the scraper and prints the data to the console
"""

import json
from scraper import scrape

with open("data.json", "w+", encoding="utf-8") as file:
    data = scrape()
    json.dump(data, file, indent=4)
