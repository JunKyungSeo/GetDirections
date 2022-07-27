from urllib.request import urlopen
from urllib.parse import quote # 한글 검색어 url에 넣어줌
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="

#start = quote(input("출발지 : "))
#stop = quote(input("도착지 : "))

start, stop = quote("사직역"), quote('부산과학고등학교')

url_ = url + start + '+' + stop
response = urlopen(url_).read()
soup = BeautifulSoup(response, "html.parser")

#print(soup.select("blind")) # <a> 태그만 추출, 결과가 list
#news = soup.find_all('a', {'class' : 'news_tit'})

apple = soup.find_all('span', attrs = {'class' : '_2zezdh_MMLf0hbxv6F5Ftv'})
print(apple)
# 여기서 해당 class가 없다고 나오는데, 이는 검색어에 따라
# 유동적으로 생성되는 class이기 때문, 이를 크롤링하려면
# selenium을 이용해아함. 
# https://conservative-vector.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%ED%81%AC%EB%A1%A4%EB%A7%81%ED%95%98%EB%8A%94%EB%8D%B0-%EA%B0%92%EC%9D%B4-%EC%95%88-%EC%9D%BD%EC%96%B4%EC%99%80%EC%A7%88%EB%95%8C-%ED%95%B4%EA%B2%B0%EB%B2%95