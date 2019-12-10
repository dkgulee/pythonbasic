from bs4 import BeautifulSoup as bs
from test_file import print_ as p
from urllib.parse import quote_plus
import requests

html = requests.get("https://www.naver.com/")    # requests로 html 그 주소의 html 내용을 가져온다
if html.status_code == 200: # 200일 경우에는 정상
    print("정상페이지")
    bs_object = bs(html.text, 'html.parser')
    # print(bs_object) -- > 네이버를 잘 가져오는지 확인
    li_tags = bs_object.findAll('li', {"class": "ca_item"})
    for i in li_tags:  # 택스트 파일 가져오는지 확인
        print(i.text)
else:
    print("오류페이지")
