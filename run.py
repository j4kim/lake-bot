"""
Description: This file runs the scraper and prints the data to the console
"""

import json
import sys
import config
import scraper
import notifier

print("Scraping new data")
new_data = scraper.scrape()

if len(new_data) == 0:
    print("Failed to scrape data, exit")
    sys.exit()

new_temperature = new_data[0]["temperature"]

try:
    with open(config.FILE, "r+", encoding="utf-8") as file:
        print("Reading old data")
        old_data = json.load(file)
        old_temperature = old_data[0]["temperature"]
except (FileNotFoundError, json.decoder.JSONDecodeError) as error:
    print("Failed to read old data from data.json:", error)
    old_temperature = 0

notifier.check_and_notify(new_temperature, old_temperature)

with open(config.FILE, "w", encoding="utf-8") as file:
    print("Writing new data")
    json.dump(new_data, file, indent=4)
