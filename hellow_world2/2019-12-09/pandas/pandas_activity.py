import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
# 작가 제목 이름
week = ["mon", "tre", "wed", "thu", "fri", "sat", "sum"]
webtoon_title = []
webtoon_img = []
webtoon_name = []
def weekly_webtoon(week):
    html = requests.get("https://comic.naver.com/webtoon/weekdayList.nhn?week={}".format(week))
    bs_object = bs(html.text, 'html.parser')
    web_list = bs_object.find("ul", {"class": "img_list"})
    for web in web_list.findAll("li"):
        is_update = web.find("em", {"class": "ico_updt"})
        if is_update != None:
            webtoon_title.append(web.find("a")["title"])
            webtoon_img.append(web.find("img")["src"])
            webtoon_name.append(web.find("dd", {"class": "desc"}).text.replace('\n', ''))
            # print("title:", web.find("a")["title"])
            # print("athor:", web.find("dd", {"class": "desc"}).text.replace('\n', ''))
            # print("img:", web.find("img")["src"])
            # print("업데이트 됨")
        else:
            webtoon_title.append(web.find("a")["title"])
            webtoon_img.append(web.find("img")["src"])
            webtoon_name.append(web.find("dd", {"class": "desc"}).text.replace('\n', ''))
            # print("title:", web.find("a")["title"])
            # print("athor:", web.find("dd", {"class": "desc"}).text.replace('\n', ''))
            # print("img:", web.find("img")["src"])
            # print("휴제입니다")


for i in week:
    print("--------------------{}----------------------".format(i))
    weekly_webtoon(week)
# df = pd.DataFrame()
data = {"타이틀": [],
        "이미지": [],
        "이름": []}
for title, name, img in zip(webtoon_title, webtoon_name, webtoon_img):
    data["타이틀"].append(title)
    data["이름"].append(name)
    data["이미지"].append(img)

df = pd.DataFrame(data)

df.to_excel('pandas.xlsx')
