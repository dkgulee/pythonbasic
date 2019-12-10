from bs4 import BeautifulSoup as bs
from test_file import print_ as p
from urllib.parse import quote_plus
import requests

html = requests.get("https://search.naver.com/search.naver?query=양천구 날씨")

print(html.status_code)

bs_object = bs(html.text, "html.parser")
print(bs_object)
add = bs_object.find("span", {"class": "btn_select"})

print(add.text)

