"""
Description: This file runs the scraper and prints the data to the console
"""

import json
import sys
from scraper import scrape

print("Scraping new data")
new_data = scrape()

if len(new_data) == 0:
    print("Failed to scrape data, exit")
    sys.exit()

old_data = []
with open("data.json", "r", encoding="utf-8") as file:
    print("Reading old data")
    try:
        old_data = json.load(file)
    except json.decoder.JSONDecodeError as error:
        print("Failed to read old data from data.json:", error)

if len(old_data) > 0:
    old_temperature = old_data[0]["temperature"]
    new_temperature = new_data[0]["temperature"]
    if old_temperature != new_temperature:
        print(f"Temperature changed from {old_temperature}° to {new_temperature}°")
    else:
        print("Temperature did not change")

with open("data.json", "w", encoding="utf-8") as file:
    print("Writing new data")
    json.dump(new_data, file, indent=4)
