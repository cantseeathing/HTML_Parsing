from bs4 import BeautifulSoup
import lxml

import requests

# response = requests.get("https://news.ycombinator.com/")
#print(response.text)

# yc_website = response.text

# soup = BeautifulSoup(yc_website, "html.parser")

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
print("-------------")
print(soup)
print("-------------")
print(soup.prettify())
print("-------------")
print(soup.title)
print(soup.title.name)
print(soup.title.text)
print(soup.title.string)
print("-------------")
print("first tag")
print(soup.a)
print(soup.li)
print(soup.p)
print("-------------")
print("find all tags")
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
for tags in all_anchor_tags:
    print(tags.get_text())

for tags in all_anchor_tags:
    print(tags.get("href"))
print("-------------")
print("find with id")
heading = soup.find_all(name="h1", id="name")
# print(all_anchor_tags)
for tags in heading:
    print(tags.get_text())
print("-------------")
print("find with class")
section_heading = soup.find_all(name="h3", class_="heading")
# print(all_anchor_tags)
for tags in section_heading:
    print(tags.get_text())
print("-------------")
print("find an element within specific tags")
company_url = soup.select(selector="p a")
for tags in company_url:
    print(tags.get_text())
# for an ID
name = soup.select(selector="#name")
for tags in name:
    print(tags.get_text())
# for a class
heading = soup.select(selector=".heading")
for tags in heading:
    print(tags.get_text())



