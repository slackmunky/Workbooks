import pandas as pd
import numpy as np

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 20)

ad_clicks = pd.read_csv(r"..\Data Files\ad_clicks.csv")

print(ad_clicks.head())
print("\n")

views_by_source = ad_clicks.groupby("utm_source").user_id.count().reset_index()
print(views_by_source)
print("\n")

ad_clicks["is_click"] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.head(20))
print("\n")

clicks_by_source = ad_clicks.groupby(["utm_source",
                                      "is_click"]).user_id.count(

).reset_index()
print(clicks_by_source)
print("\n")

clicks_pivot = clicks_by_source.pivot(
        columns="is_click",
        index="utm_source",
        values="user_id"
).reset_index()
print(clicks_pivot)
print("\n")

clicks_pivot["percent_clicked"] = clicks_pivot[True] / (clicks_pivot[True] +
                                                        clicks_pivot[False])
print(clicks_pivot)
print("\n")

ad_group = ad_clicks.groupby(
        "experimental_group").user_id.count().reset_index()
print(ad_group)
print("\n")

ad_group_clicks = ad_clicks.groupby(["is_click",
                                     "experimental_group"]).user_id.count(

).reset_index()
print(ad_group_clicks)
print("\n")

ad_group_clicks_pivot = ad_group_clicks.pivot(
        columns="is_click",
        index="experimental_group",
        values="user_id"
).reset_index()
print(ad_group_clicks_pivot)
print("\n")

ad_group_clicks_pivot["percent_clicked"] = ad_group_clicks_pivot[True] / (
        ad_group_clicks_pivot[True] + ad_group_clicks_pivot[False])
print(ad_group_clicks_pivot)
print("\n")

a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]
print(a_clicks.head())
print("\n")
print(b_clicks.head())
print("\n")

a_clicks_daily = a_clicks.groupby(["day", "is_click"]).user_id.count(

).reset_index()
a_clicks_daily_pivot = a_clicks_daily.pivot(
        columns="is_click",
        index="day",
        values="user_id"
).reset_index()
a_clicks_daily_pivot["percent_clicked"] = a_clicks_daily_pivot[True] / (
        a_clicks_daily_pivot[True] + a_clicks_daily_pivot[False])
print(a_clicks_daily_pivot)
print("\n")

b_clicks_daily = b_clicks.groupby(
        ["day", "is_click"]).user_id.count().reset_index()
b_clicks_daily_pivot = b_clicks_daily.pivot(
        columns="is_click",
        index="day",
        values="user_id"
).reset_index()
b_clicks_daily_pivot["percent_clicked"] = b_clicks_daily_pivot[True] / (
        b_clicks_daily_pivot[True] + b_clicks_daily_pivot[False])
print(b_clicks_daily_pivot)
print("\n")
