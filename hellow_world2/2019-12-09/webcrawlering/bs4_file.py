from bs4 import BeautifulSoup as bs
from test_file import print_ as p
html = """
<!DOCTYPE html>
<html>
   <head>
       <title>웹 크롤링 실습</title>
   </head>
<body>
   <h1 class="green">1. 웹 크롤링 실습 페이지 입니다.</h1>
   <h1 class="red">2. 웹 크롤링 실습 페이지 입니다.</h1>
   <p>웹 크롤링 실습 p 태그 입니다.</p>
</body>
</html>"""

bs_object = bs(html, "html.parser") # 파싱된 오브잭트이다
print(bs_object.find("h1")) # <h1 class="green">1. 웹 크롤링 실습 페이지 입니다.</h1>
p.under_line(20)
print(bs_object.find("h1").text) #1. 웹 크롤링 실습 페이지 입니다.
p.under_line(20)
print(bs_object.find_all("h1")) # list 로 가져온다
print(type(bs_object.find_all("h1")))  # class
p.under_line(20)
all_find = bs_object.find_all("h1")
for i in all_find:
    print(i)
p.under_line(20)
for i in all_find:
    print(i.text)
p.under_line(20)

h1_tag_red = bs_object.find('h1', {"class": "red"})
h1_tag = bs_object.find('h1', {"class": {'red': 'green'}}) #첫번쨰것이 나온다
h1_tag_all = bs_object.find_all('h1', {'class': {'red': 'green'}})
print(h1_tag_red)
print(h1_tag)
print(h1_tag_all)
p.under_line(20)
for i in h1_tag_all:
    print(i.text)

