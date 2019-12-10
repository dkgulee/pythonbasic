from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# 1 -> 1  2 ->11 3 - >21
naver_title = []
naver_content = []
naver_url = []
def finding_naver(search, page):
    page = 10 * page - 9
    for num in range(page):
        url = "https://search.naver.com/search.naver?where=post&sm=tab_jum&query={ㅁㄴㅇㄻㄴㅇㄻㄶ}&sm=tab_pge&srchby=all&st=sim&where=post&start={}".format(search, num)
        html = requests.get(url)
        soup = bs(html.text, "html.parser")
        for i in soup.findAll("li", {"class": "sh_blog_top"}):
            print(i.find("a", {"class": "sh_blog_title"}).text)
            naver_title.append(i.find("a", {"class": "sh_blog_title"}).text)
            print(i.find("dd", {"class": "sh_blog_passage"}).text)
            naver_content.append(i.find("dd", {"class": "sh_blog_passage"}).text)
            print(i.find("a")["href"])
            naver_url.append(i.find("a")["href"])

search = input("무슨 블로그를 검색 하시겠습니까?:")
page = int(input("몇 페이지를 검색 하시겠습니까?:"))
finding_naver(search, page)
naver_data = {"타이틀": naver_title,
             "content": naver_content,
             "url": naver_url}
print(naver_data)
df = pd.DataFrame(naver_data)
df.to_excel("{}_{}.xlsx".format(search, str(page)))

pd.read_excel