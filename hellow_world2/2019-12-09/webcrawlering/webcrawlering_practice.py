from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
# 웹 제안명과 안의 네용을 보는 것!

def goverment(n):
    url = "https://www.innogov.go.kr/ucms/bbs/B0000042/list.do?sort=02&searchCnd=1&searchWrd=&pageIndex={}&menuNo=300125".format(
        str(n))
    html = requests.get(url)
    soup = bs(html.text, "html.parser")

    goverment_title = []
    goverment_value = []

    for name in soup.findAll("td", {"class": "tit"}):
        # print(name.text)
        goverment_title.append(name.text)
        new_url = "https://www.innogov.go.kr{}".format(name.find("a")["href"])
        # print(new_url)
        html = requests.get(new_url)
        soup = bs(html.text, "html.parser")
        # print(soup.find("div", {"class": "dbData"}).text)
        goverment_value.append(soup.find("div", {"class": "dbData"}).text)

    # print(goverment_title)
    # print(goverment_value)

    data = {"제목": [],
            "내용": []}
    for title, value in zip(goverment_title, goverment_value):
        data["제목"].append(title)
        data["내용"].append(value)
    df = pd.DataFrame(data)
    df.to_excel('goverment{}.xlsx'.format(n))

goverment(input("번호를 입력하세요:"))