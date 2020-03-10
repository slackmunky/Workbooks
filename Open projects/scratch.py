import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import openpyxl
import re

desired_width = 320
# pd.set_option('display.max_colwidth', 25)
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', None)

# mh_response = requests.get(r"https://www.mohawkaustin.com/events/")
# mh_content = mh_response.content
# mh_soup = BeautifulSoup(mh_content, features="html.parser")

try:
    mh_soup = BeautifulSoup(
        open(r"..\Data Files\mohawk_test.html"), features="html.parser")
except FileNotFoundError:
    mh_soup = BeautifulSoup(open(r"Data Files\mohawk_test.html"),
                            features="html.parser")

show_list_main = mh_soup.select(".list-view-item")  # MAIN
artist_info = mh_soup.select(".artist-info")
presenting = mh_soup.select(".artist-info")  # DONE DONE DONE
headliners = mh_soup.select(".headliners")  # DONE DONE DONE
dates = mh_soup.select(".date-time")  # DONE DONE DONE
supporting = mh_soup.select(".artist-info")  # DONE DONE DONE
show_pages = mh_soup.findAll("button",
                             href=re.compile("https"),
                             # class_="primary-link"
                             )
show_time = mh_soup.select(".start")  # DONE DONE DONE
ages = mh_soup.select(".date-age")  # DONE DONE DONE
# May need to hold off on this one. Maybe do links first...
prices = mh_soup.select(".ticket-price")


# link_test = artist_info

# for item in link_test:
# print(item)


def get_links(source):
    links = []
    for link in source:
        links.append(link.get('href'))
    print("link list len:", len(links))
    counter = 1
    fun_dict = {"mohawk_0": ["list_id", "show_link"]}
    fun_dict["mohawk_0"].insert(0, "list_id")
    key = "mohawk_" + str(counter)
    for entry in links:
        # print(entry)
        fun_dict[key] = [counter, entry]
        show = [counter, entry]
        while len(show) < len(fun_dict["mohawk_0"]):
            show.append("NVal")
            fun_dict[key] += show
        counter += 1
    # print(links)
    print("link dict len:", len(fun_dict))
    return fun_dict


# print(show_pages)
# get_links(show_pages)


def null_val(item_to_test):
    if type(item_to_test) == None:
        return "NVal"
    return item_to_test


def mh_get_info(data_group, columns, tag_name):
    if type(tag_name) is not str:
        return print("tag_name must be a string.")
    for item in columns:
        if type(item) is not str:
            return print("columns must be a list of strings.")
    counter = 1
    fun_dict = {"mohawk_0": columns}
    fun_dict["mohawk_0"].insert(0, "list_id")
    fun_dict["mohawk_0"].insert(1, "show_link")
    for item in data_group:
        key = "mohawk_" + str(counter)
        fun_dict[key] = []
        data_group = list(item.find_all(tag_name))
        show = [counter]
        try:
            show_link = item.find("a", href=re.compile("https")).get("href")
            show.append(show_link)
        except AttributeError:
            pass
        for entry in data_group:
            entry_text = entry.get_text()
            show.append(entry_text)
        while len(show) < len(fun_dict["mohawk_0"]):
            show.append("NVal")
        fun_dict[key] += show
        counter += 1
    # print(fun_dict)
    return fun_dict


def create_df(info_dict):
    info_df = pd.DataFrame(info_dict)
    # info_df_transposed = info_df.transpose()
    # info_df_transposed.to_excel(r"..\Data Files\mohawk_test_out.xlsx")
    # print(info_df_transposed.head())
    # return info_df_transposed
    return (info_df)


# ARTIST_INFO, PRESENTING, AND SUPPORTING ALL USE THE SAME DATA GROUP
# MAYBE THINK ABOUT GROUPING THOSE UP.

price_list = mh_get_info(prices, ["ticket_price", "col_2"], "span")
price_sheet = create_df(price_list)

date_age = mh_get_info(ages, ["time", "age_restriction"], "section")
date_age_sheet = create_df(date_age)

supporting_acts = mh_get_info(supporting, ["supported_by"], "h2")
support_sheet = create_df(supporting_acts)

presented_by = mh_get_info(presenting, ["presented_by"], "section")
presenter_sheet = create_df(presented_by)

date_time = mh_get_info(dates, ["date", "time"], "span")
schedule_sheet = create_df(date_time)

hl_dict = mh_get_info(artist_info,
                      ["headliner_1", "headliner_2"],
                      "h1")
headliner_df = create_df(hl_dict)

# version_1 = pd.merge(support_sheet,
#                       headliner_df,
#                       how="outer")
# test_final = version_1.merge(schedule_sheet, presenter_sheet, how="outer")

to_join = [date_age_sheet, support_sheet, presenter_sheet, schedule_sheet, headliner_df]
test_final = pd.concat(to_join, join="outer")
trans_final = test_final.transpose()
trans_final.to_excel(r"..\Data Files\mohawk_test_out.xlsx")
