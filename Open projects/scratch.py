import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import openpyxl

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', None)

mh_soup = BeautifulSoup(open(r"..\Data Files\mohawk_test.html"),
                        features="html.parser")

show_list_main = mh_soup.select(".list-view-item")
presenting = mh_soup.select(".presented-by")
headliners = mh_soup.select(".headliners")
dates = mh_soup.select(".dates")  # Done and used as dict keys.
supporting = mh_soup.select(".supports")
show_pages = mh_soup.select(".image-url")
show_time = mh_soup.selet(".start")
ages = mh_soup.select(".age-restriction")
prices = mh_soup.select(".price-range")

date_keys = []  # COMPLETED
for date in dates:
    mh_key = "mohawk_" + date.string.replace(
            ", ", "_").replace(" ", "_").lower()
    date_keys.append(str(mh_key))
#print(date_keys)
#print(artists[0])
headliner_list = []
for act in headliners:
    artist = str(act.string)
    headliner_list += artist
#print("acts:", len(headliner_list))
print(headliner_list[:5])

links = []
for link in show_pages:
    lnk = str(link.string)
    links.append(lnk)
#print(links)

# event_text = {}
# counter = 0
# for item in show_list_main:
#     key = date_keys[counter]
#     event_text[key] = []
#     details = list(item.stripped_strings)
#     event_text[key] = details
#     counter += 1
