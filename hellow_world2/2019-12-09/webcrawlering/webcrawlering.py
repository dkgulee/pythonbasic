import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup as bs
from selenium import webdriver
search = input("검색은? :")
html = requests.get('https://www.google.com/search?q={}'.format(quote_plus(search)))


driver = webdriver.Chrome()
driver.get(html)

html = driver.page_source
print(html)


