import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import openpyxl

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', None)
# mh_soup = BeautifulSoup(open(r"..\Data Files\mohawk_test.html"),
#                         features="html.parser") Open projects\html_scratch.htm
mh_soup = BeautifulSoup(open(r"Data Files\mohawk_test.html"),
                        features="html.parser")  # -item

show_list_main = mh_soup.select(".list-view-item")
artist_info = mh_soup.find("article", class_="artist-info")
# presenting = mh_soup.select(".presented-by")
# headliners = mh_soup.select(".headliners")
dates = mh_soup.select(".dates")  # Done and used as dict keys.
# supporting = mh_soup.select(".supports")
show_pages = mh_soup.select(".image-url")
show_time = mh_soup.select(".start")
ages = mh_soup.select(".age-restriction")
prices = mh_soup.select(".price-range")

# date_keys = []  # COMPLETED
# for date in dates:
#     mh_key = "mohawk_" + date.string.replace(
#             ", ", "_").replace(" ", "_").lower()
#     date_keys.append(str(mh_key))

def null_val(object):
    str(object)
    if object == None:
        return "NVal"
    return object


# artist_list = {}
# article = list(artist_info.find_all("h1", class_="headliners"))
# counter = 1
# for show in show_list_main:
    # key = counter
    # headliners = artist_info.find_all("h1", class_="headliners")
    # for artist in headliners:
    #     headliner = artist_info.h1.string.replace("\n                   ", "")
    #     playbill = []
    #     playbill += headliner
    #     artist_list[key] = (playbill)
    # artist_list[key] = list(artist_info.h1.string)
    # print(headliner)
    # counter += 1

# print(artist_list)

# print(count[:10])



show_notes: []



# print(artist_info)


#print(date_keys)
#print(artists[0])
#headliner_list = []
#for act in headliners:
#    artist = str(act.string)
#    headliner_list.append(artist)
#print("acts:", len(headliner_list))
#print(headliner_list)

links = []
for link in show_pages:
    lnk = str(link.string)
    links.append(lnk)
#print(links)

event_text = {}
counter = 0
for item in show_list_main:
    key = "mohawk_" + str(counter)
    event_text[key] = []
    details = list(item.stripped_strings)
    event_text[key] = details
    while len(details) < 10:
        details.append("NVal")
    counter += 1


event_df = pd.DataFrame(event_text)
event_df_transposed = event_df.transpose()
event_df_transposed.to_excel(r"Data Files\mohawk_test_out.xlsx")