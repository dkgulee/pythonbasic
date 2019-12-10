import requests
from bs4 import BeautifulSoup as bs
# 작가 제목 이름
week = ["mon", "tre", "wed", "thu", "fri", "sat", "sum"]
webtoon_title = []
webtoon_img = []
def weekly_webtoon(week):
    html = requests.get("https://comic.naver.com/webtoon/weekdayList.nhn?week={}".format(week))
    bs_object = bs(html.text, 'html.parser')
    web_list = bs_object.find("ul", {"class": "img_list"})
    for web in web_list.findAll("li"):
        is_update = web.find("em", {"class": "ico_updt"})
        if is_update != None:
            webtoon_title.append(web.find("a")["title"])
            webtoon_img.append(web.find("img")["src"])
            print("title:", web.find("a")["title"])
            print("athor:", web.find("dd", {"class": "desc"}).text.replace('\n', ''))
            print("img:", web.find("img")["src"])
            print("업데이트 됨")
        else:
            webtoon_title.append(web.find("a")["title"])
            webtoon_img.append(web.find("img")["src"])
            print("title:", web.find("a")["title"])
            print("athor:", web.find("dd", {"class": "desc"}).text.replace('\n', ''))
            print("img:", web.find("img")["src"])
            print("휴제입니다")


for i in week:
    print("--------------------{}----------------------".format(i))
    weekly_webtoon(week)

html = """
<!doctype html>
<html lang="ko">
   <head>
   <meta charset="utf-8">
      <title>HTML</title>
   </head>
   <body>"""
for title, img in zip(webtoon_title, webtoon_img):
    html +="<img scr=\"" + img + "\">" + title + "</img>\n"


html += """
   </body>
</html>
"""

file = open("webtoon.html", "w", encoding="UTF-8")
file.write(html)
file.close()