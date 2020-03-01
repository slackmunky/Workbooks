import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', None)

# noinspection SpellCheckingInspection
webpage_response = requests.get(
        'https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup'
        '/shellter.html')
webpage = webpage_response.content
# webpage_response2 = requests.get("https://en.wikipedia.org/wiki/Python_("
#                                  "programming_language)")
# webpage2 = webpage_response2.content


ca_test = requests.get("https://www.codecademy.com/courses/learn-web-scraping/lessons/web-scraping-with-beautiful-soup/exercises/website-structure")
ca_test_content = ca_test.content
ca_soup = BeautifulSoup(ca_test_content, features="html.parser")
# print(ca_soup)
first_para = ".html.body.div[1].section.div.div.div[1].div[1].div.div[2].div[2].div.div[2].p[1].text()"
print(ca_soup.body.div)

# The difference between ".text" and ".content" is that text is laid out in
# html style and content is just messy block of code.
# print(webpage.text)
# print(webpage.content)

# MAKE SURE YOU USE THE "features="html.parser"" ARGUMENT. OR ELSE...!
soup = BeautifulSoup(webpage, features="html.parser")
# soup2 = BeautifulSoup(webpage2, features="html.parser")
# print(soup)

# Selecting/printing an element: "p" for the html "paragraph" element.
#print(soup.p)
# Selecting/printing smaller elements: the string inside the paragraph.
#print(soup.p.string)
# print()
# Selecting/printing each child of an element
#for child in soup.div.children:
#    print(child)

#prefix = "https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/"

# The ".find_all" function.
# turtle_links = soup.find_all("a")
# links = []
# for a in turtle_links:
#     links.append(prefix + a["href"])
#
# turtle_data = {}
#
# for link in links:
#     webpage = requests.get(link)
#     turtle = BeautifulSoup(webpage.content, "html.parser")
#     turtle_name = turtle.select(".name")[0].get_text()

#     stats = turtle.find("ul")
#     stats_text = stats.get_text("|")

#     turtle_data[turtle_name] = stats_text.split("|")
#
# print(turtle_data)

