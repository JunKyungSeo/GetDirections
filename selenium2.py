# pip install selenium
from selenium import webdriver
from urllib.parse import quote
import time
import os

class getDirections:
    def __init__(self):
        try:
            driver = webdriver.Chrome('chromedriver.exe')
        except:
            print('chromedriver.exe 실행 오류')
            return None
        
    def getTime(self, start, stop):
        
        url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="

        #start, stop = quote(input("출발지 : ")), quote(input("도착지 : "))
        start, stop = quote("사직역"), quote('부산과학고등학교')
        url_ = url + start + quote('에서') + '+' + stop

        driver = webdriver.Chrome("chromedriver.exe")
        driver.get(url_)

        # xpath1 : '최적' 시간
        #xpath1 = '//*[@id="main_pack"]/section[1]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/ul/li[1]/div/div[1]/button[1]/dl/div[1]/dd/span/span[1]'
        #content1 = driver.find_element("xpath", xpath1)
        #content1_time = content1.text

        # xpath2 : '지하철' 시간
        xpath2_1 = '//*[@id="main_pack"]/section[1]/div/div/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div/ul/li[3]/button'
        time.sleep(3)
        driver.find_element("xpath", xpath2_1).click() # "지하철" 버튼 클릭, 지하철 경로만 보이도록 함
        xpath2_2 = '//*[@id="main_pack"]/section[1]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/ul/li[1]/div/div[1]/button[1]/dl/div[1]/dd/span/span[1]'
        content2 = driver.find_element("xpath", xpath2_2)
        content2_time = content2.text
        driver.quit
        return content2_time

if __name__=="__main__":
    try1 = getDirections()
    print(try1.getTime(1, 2))