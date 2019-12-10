from bs4 import BeautifulSoup as bs
from test_file import print_ as p
from urllib.parse import quote_plus
import requests



def naver_we(address):
    html = requests.get('https://search.naver.com/search.naver?query={}+날씨'.format(address))
    bs_object = bs(html.text, "html.parser")
    address = bs_object.find("span", {"class": "btn_select"})
    temp = bs_object.find('span', {"class": "todaytemp"})
    indicator_tag = bs_object.find('dl', {'class': 'indicator'})
    dd_tags = indicator_tag.findAll('span', {'class': 'num'})
    print("{}의 날씨는 {}도 입니다.".format(address.text, temp.text))
    text_dd = ["미세먼지", "초미세먼지", "오존지수"]
    # for i in dd_tags:
    #     print(i.text)
    # for text, tag in zip(text_dd, dd_tags):
    #     print(text, tag.text)
    #
    # for i, tag in enumerate(dd_tags, 1):
    #     print(i, tag.text)

add =["양천구", "강남구", "관악구"]
for address in add:
    naver_we(address)

search = input("날씨를 입력하세요:")

naver_we(search)