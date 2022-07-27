# https://beomi.github.io/gb-crawling/posts/2017-02-27-HowToMakeWebCrawler-With-Selenium.html
# https://pythondocs.net/selenium/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%ED%81%AC%EB%A1%A4%EB%9F%AC-%EA%B8%B0%EB%B3%B8-%EC%82%AC%EC%9A%A9%EB%B2%95/

# pip install selenium
from selenium import webdriver
# from urllib.request import urlopen
from urllib.parse import quote # 한글 검색어 url에 넣어줌
# from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By #find element by xpath 오류 해결 위해

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="

#start = quote(input("출발지 : "))
#stop = quote(input("도착지 : "))

start, stop = quote("사직역"), quote('부산과학고등학교')

url_ = url + start + quote('에서') + '+' + stop

driver = webdriver.Chrome("chromedriver.exe")
#'./Users/sjkda/Downloads/chromedriver')
# 원래 selenium은 웹이 다 로드될 때까지 기다려주지만,
# 암묵적으로 이걸 지정해주기도 함
driver.implicitly_wait(5)
driver.get(url_)

xpath = '//*[@id="main_pack"]/section[1]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/ul/li[1]/div/div[1]/button[1]/dl/div[1]/dd/span/span[1]'
# xpath로 네이버 길찾기에서 '최적'이라 표시되는 시간 지정

apple = driver.find_element("xpath", xpath)

print(apple.text) # '최적' 시간 표시
print(type(apple.text))

driver.quit() # 현재 탭 닫기


#<span class="_2zezdh_MMLf0hbxv6F5Ftv">51</span>
#main_pack > section:nth-child(7) > div > div > div > div:nth-child(2) > div:nth-child(3) > div > div._3wcvt8MIGDgyop9tWDL3aj > div:nth-child(2) > ul > li:nth-child(1) > div > div._1KtGx95AHp_3_XzQGfCtJT > button._6dxTh1Q1zE9UbHXa_QSSr._1DAbtmbjrcgcgrbObR015._2Hlf6pmVy-tE5i3o5NUmMk > dl > div:nth-child(1) > dd > span > span._2zezdh_MMLf0hbxv6F5Ftv
#document.querySelector("#main_pack > section:nth-child(7) > div > div > div > div:nth-child(2) > div:nth-child(3) > div > div._3wcvt8MIGDgyop9tWDL3aj > div:nth-child(2) > ul > li:nth-child(1) > div > div._1KtGx95AHp_3_XzQGfCtJT > button._6dxTh1Q1zE9UbHXa_QSSr._1DAbtmbjrcgcgrbObR015._2Hlf6pmVy-tE5i3o5NUmMk > dl > div:nth-child(1) > dd > span > span._2zezdh_MMLf0hbxv6F5Ftv")
#//*[@id="main_pack"]/section[1]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/ul/li[1]/div/div[1]/button[1]/dl/div[1]/dd/span/span[1]
#/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/ul/li[1]/div/div[1]/button[1]/dl/div[1]/dd/span/span[1]
#"//div[@class='style__ShopProductSubCategoryChip-sc-1bc3ssb-2 iKSeHs']"