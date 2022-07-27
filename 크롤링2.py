# pip install requests

# requests 라이브러리가 urllib 보다 편하고 빠름
import requests
response = requests.get("https://www.naver.com")

# print(response.status_code)
# print(response.headers['content-type'])
# print(response.encoding)
# print(response.text)

# html 을 분석 가능한 형태로 가능할 수 있는 bs import
# pip install BeautifulSoup4d
# html을 해석하는 해석 라이브러리, bs랑 연동 
# pip install lxml

from bs4 import BeautifulSoup
bs = BeautifulSoup(response.text, "html.parser")
print(bs.select("a")) # <a> 태그만 추출, 결과가 list

