from bs4 import BeautifulSoup as bs
import requests

add = ["양천구 날씨", "강남구 날씨", "관악구 날씨"]
for i in add:
    html = requests.get("https://search.naver.com/search.naver?query={}날씨".format(i))

    bs_object = bs(html.text, "html.parser")
    address = [bs_object.find("span", {"class": "btn_select"})]
    temp = bs_object.find('span', {"class": "todaytemp"})
    print("{}의 날씨 : {}".format(i, temp.text))
    # indicator_tag = bs_object.find('dl', {'class': 'indicator'})
    # dd_tags = indicator_tag.findAll('span', {'class': 'num'})

