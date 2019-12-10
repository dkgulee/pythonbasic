import requests
from bs4 import BeautifulSoup as bs

html = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
bs_object = bs(html.text, 'html.parser')

webtoon_all_tag = bs_object.find("div", {"class": "list_area daily_all"})
#print(webtoon_all_tag)

for webtoom in webtoon_all_tag.findAll("li"):
    print(webtoom.find("a", {"class": "title"}).text)
    print(webtoom.find("img")["src"])