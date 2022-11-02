from bs4 import BeautifulSoup
import lxml

import requests

response = requests.get("https://news.ycombinator.com/")
print(response.text)

yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")
# print("---------")
# article_text = soup.find_all(name="span", class_="titleline")
# for tags in article_text:
#     print(tags.get_text())
# print("---------")
# article_link = soup.select(selector=".titleline")
# for tags in article_link:
#     print(tags.get_text())
# print("---------")
# article_votes = soup.select(selector=".score")
# for tags in article_votes:
#     print(tags.get_text())

news = soup.find_all(class_="titleline")
for heading in news:
    print(heading.find(name="a").getText())

for heading in news:
    print(heading.find(name="a").get("href"))

scores = soup.find_all(class_="score")
for score in scores:
    print(score.getText().split(" ")[0])

# # notice that the anchor tag is inside of a <span> with class="titleline"
#
# article_text = soup.find(name="span", class_="titleline").find(name="a").get_text()
#
# # or something easier to understand
#
# first_article_span = soup.find(name="span", class_="titleline")
# first_article_anchor_tag = first_article_span.find(name="a")
# first_article_text = first_article_anchor_tag.get_text()