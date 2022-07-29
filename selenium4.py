# pip install selenium
from selenium import webdriver
from urllib.parse import quote
import time
import os
from selenium.webdriver.common.by import By

# 아래 5줄 : 없어도 되긴 한데, 오류 메세지 떠서 붙여넣음
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
        
class getDirections:
    def __init__(self, start = '사직역', stop = '부산과학고등학교'):
        '(출발지, 도착지)'
        self.start = start
        self.stop = stop
        url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="
        start, stop = quote(self.start), quote(self.stop)
        self.url_ = url + start + quote('에서') + '+' + stop
        xpath_box = '//*[@id="main_pack"]/section[1]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/ul' # 상자 xpath
        
        finish = False
        while not finish:
            which_path = '0' #input('최적 [0] or 최소 시간 [1] ? : ')
            
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.get(self.url_)
            time.sleep(10)
            content1 = driver.find_element("xpath", xpath_box)
            content2 = driver.find_elements(By.CLASS_NAME, "_10HIlqQetVgP4lkyO81GDY")
            print(type(content2), len(content2))
            for i in content2:
                print(i.text)
            driver.quit
            
            if which_path == '1':
                # 최적이랑 최소 시간이 같으면 최적으로 표시됨
                xpath__ = '//*[@id="main_pack"]/section[1]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/ul/li[3]/div/div[1]/button[1]/em'
                
                
                if content1.text == '최소시간':
                    self.xpath1 = '//*[@id="main_pack"]/section[1]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/ul/li[3]/div/div[1]/button[1]/dl/div[1]/dd/span/span[1]'
                    self.xpath2 = ''
                    # path2 : 정보 들어있는 네모 칸
                    finish = True
                    break
                else:
                    which_path = '0'
                    
            elif which_path == '0':
                self.xpath1 = '//*[@id="main_pack"]/section[1]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/ul/li[1]/div/div[1]/button[1]/dl/div[1]/dd/span/span[1]'
                self.xpath2 = '//*[@id="main_pack"]/section[1]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/ul[1]/li/div/div[2]/div/ol'
                # path2 : 정보 들어있는 네모 칸
                finish = True
            else:
                print('Please Retry')
    
    def UseSubway(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(self.url_)
        time.sleep(3)
        content1 = driver.find_element("xpath", '//*[@id="main_pack"]/section[1]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/ul')#self.xpath2)
        source_code1 = content1.get_attribute("outerHTML")
        driver.quit
        return source_code1
        
    def getTime(self):
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(self.url_)
        content_time = driver.find_element("xpath", self.xpath1).text
        driver.quit
        return content_time
    
class aaa(getDirections):
    def __init__(self):
        pass
        
        
필요한_함수 = """ 
    1. 최적 경로로 갈건지 혹은 최소 시간 경로로 갈건지
    2. 해당 경로에 지하철을 이용하는게 있는지. (지하철 이용이 없다면 택시 이용이 가장 빠른게 확정됨)
    3. 지하철을 이용할 때, 어떤 역을 지나는지
    4. 택시로 해당 역까지 가서 지하철 타는 시간과, 지하철 타고 해당 역까지 가서 택시 타는 거 시간 비교, 다음 목적지까지
    - 이때 다음 목적지는 최종 목적지 or 다음으로 지하철을 타기 시작하는 장소
    """

if __name__=="__main__":
    try1 = getDirections() #'사직역', '서면역')
    # print(try1.UseSubway())
    # print(try1.getTime(1, 2))