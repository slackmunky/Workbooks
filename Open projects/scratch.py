import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import openpyxl

desired_width = 320
# pd.set_option('display.max_colwidth', 25)
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', None)
# mh_soup = BeautifulSoup(open(r"..\Data Files\mohawk_test.html"),
#                         features="html.parser") Open
#                         projects\html_scratch.htm
mh_soup = BeautifulSoup(open(r"..\Data Files\mohawk_test.html"),
                        features="html.parser")  # -item

show_list_main = mh_soup.select(".list-view-item")  # MAIN
artist_info = mh_soup.select(".artist-info")
presenting = mh_soup.select(".artist-info")  # DONE DONE DONE
headliners = mh_soup.select(".headliners")  # DONE DONE DONE
dates = mh_soup.select(".date-time")  # DONE DONE DONE
supporting = mh_soup.select(".artist-info")  # DONE DONE DONE
show_pages = mh_soup.select(".image-url")
show_time = mh_soup.select(".start")  # DONE DONE DONE
ages = mh_soup.select(".date-age")  # DONE DONE DONE
prices = mh_soup.select(".ticket-price")  # May need to hold off on this one. Maybe do links first...

for item in prices:
    print(item)


def mh_get_info(data_group, columns, tag_name):
    if type(tag_name) is not str:
        return print("tag_name must be a string.")
    for item in columns:
        if type(item) is not str:
            return print("columns must be a list of strings.")
    counter = 1
    fun_dict = {"mohawk_0": columns}
    fun_dict["mohawk_0"].insert(0, "list_id")
    for item in data_group:
        key = "mohawk_" + str(counter)
        fun_dict[key] = []
        data_group = list(item.find_all(tag_name))
        show = [counter]
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
    info_df_transposed = info_df.transpose()
    # info_df_transposed.to_excel(r"..\Data Files\mohawk_test_out.xlsx")
    print(info_df_transposed)
    return info_df_transposed


# price_list = mh_get_info(prices, ["ticket_price", "col_2"], "span")
# price_sheet = create_df(price_list)

# date_age = mh_get_info(ages, ["time", "age_restriction"], "section")
# date_age_sheet = create_df(for_ages)

# supporting_acts = mh_get_info(supporting, ["supported_by"], "h2")
# support_sheet = create_df(supporting_acts)

# presented_by = mh_get_info(presenting, ["presented_by"], "section")
# presenter_sheet = create_df(presented_by)

# date_time = mh_get_info(dates, ["date", "time"], "span")
# schedule_sheet = create_df(date_time)
# hl_dict = mh_get_info(artist_info,
#                       ["headliner_1", "headliner_2"],
#                       "h1")
# headliner_df = create_df(hl_dict)


def null_val(item_to_test):
    if type(item_to_test) == None:
        return "NVal"
    return item_to_test
