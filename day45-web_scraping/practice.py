from bs4 import BeautifulSoup
# import lxml
import requests

response = requests.get("https://news.ycombinator.com/")
y_comb_news = response.text

soup = BeautifulSoup(y_comb_news, "html.parser")


articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.find("a")
    article_texts.append(text.getText())
    link = text.get("href")
    article_links.append(link)

article_upvotes = [int(article.getText().split()[0]) for article in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

index = article_upvotes.index(max(article_upvotes))
print(article_links[index], article_texts[index])

# article_upvotes = soup.find(name="span", class_="score")
# print(article_upvotes.getText())

# print(soup.find(class_="votelinks").getText())
# print(soup.find(class_="titleline").getText())


# links = soup.find_all(class_="titleline")
# for link in links[0]:
#     print(link.getText())

























# with open("website.html", "r") as txt:
#     contents = txt.read()

# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.li)

# # list_tags = soup.find_all(name="a")


# # for tag in list_tags:
# #     print(tag.getText())

# print(soup.find(name="h1", id="name"))

# heading = soup.find(name="h3", class_="heading")
# print(heading.get("class"))

# first_link = soup.select_one(selector="p a")
# print(first_link)