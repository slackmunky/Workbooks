import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import openpyxl

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', None)

ss_main = requests.get("https://www.austinshowspot.com/")
# ss_content = ss_main.content
ss_soup = BeautifulSoup(ss_main.content, features="html.parser")

tbody = ss_soup.find("tbody")

big_money = {}
table_rows = ss_soup.select("tr")

counter = 1
row_list = []

for row in table_rows:
    row_text = row.get_text("||")
    row_list = row_text.split("||")
    while len(row_list) < 15:
        row_list.append("fill")
    big_money[counter] = row_list
    counter += 1


#for key in big_money:
    #while len(big_money[key]):

df_bm = pd.DataFrame(big_money)
df_bm_transposed = df_bm.transpose()
#print(df_bm)

df_bm_transposed.to_excel(r"..\Data Files\show_spot_test.xlsx")
#     stats = turtle.find("ul")
#     stats_text = stats.get_text("|")
#     turtle_data[turtle_name] = stats_text.split("|")
#for key in big_money:
#    print(big_money[key])




# for column in column3:
#     try:
#         count = 1
#         print(type(item))
#         date_text = item.get_text()
#         details = [date_text]
#         #deets = item.find("td")
#         #print(type(deets))
#         #deets_text = deets.get_text("||")
#         #details.extend(deets)
#         big_money[count] = [details]
#     except TypeError:
#         print("Big ol' None in there.")

# print(big_money)

#     stats = turtle.find("ul")
#     stats_text = stats.get_text("|")
#     turtle_data[turtle_name] = stats_text.split("|")

