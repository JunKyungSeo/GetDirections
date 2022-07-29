# selenium2.py 문제 : 지하철 이용 시, 도중에 어떤 역을 지나는지 알 수 없음
# 해결 방법 : 지하철 노선도 정보를 미리 입력해두거나, 혹은 네이버 지도 사이트 크롤링

# 네이버 지도 사이트
# https://map.naver.com/v5/directions/-/-/-/transit?c=14367086.3761935,4188376.5598050,15,0,0,0,dh
# https://map.naver.com/v5/directions/14367471.81993037,4190900.7433043383,%EC%82%AC%EC%A7%81%EC%97%AD%20%EB%B6%80%EC%82%B03%ED%98%B8%EC%84%A0,70308,SUBWAY_STATION/14369404.059123773,4199752.201668847,%EB%B6%80%EC%82%B0%EA%B3%BC%ED%95%99%EA%B3%A0%EB%93%B1%ED%95%99%EA%B5%90,12182637,PLACE_POI/-/transit?c=14365048.3723519,4195365.8853457,12,0,0,0,dh
# 사직역 -> 부산과학고등학교
# 사직역 -> 서면역
# https://map.naver.com/v5/directions/14367471.81993037,4190900.7433043383,%EC%82%AC%EC%A7%81%EC%97%AD%20%EB%B6%80%EC%82%B03%ED%98%B8%EC%84%A0,70308,SUBWAY_STATION/14366825.042556915,4185386.826763142,%EC%84%9C%EB%A9%B4%EC%97%AD%20%EB%B6%80%EC%82%B01%ED%98%B8%EC%84%A0,70119,SUBWAY_STATION/-/transit?c=14364349.8648111,4188143.8979992,12,0,0,0,dh

# 링크를 직접적으로 수정하는건 힘들 것 같고, selenium 으로 텍스트 입력 후 길찾기를 누르는 것으로.
# 이것도 지하철 역과 역 사이에서만 이거 이용
# * 네이버 open api를 이용하면 되지만, 월 6만원씩 돈을 내야함.

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
        
        finish = False
        while not finish:
            which_path = input('최적 [0] or 최소 시간 [1] ? : ')
            
            if which_path == '1':
                # 최적이랑 최소 시간이 같으면 최적으로 표시됨
                xpath__ = '//*[@id="main_pack"]/section[1]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/ul/li[3]/div/div[1]/button[1]/em'
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                driver.get(self.url_)
                content1 = driver.find_element("xpath", xpath__)
                driver.quit
                
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
        # 이거 왜 xpath 인식이 안되냐 -> time.sleep(3) 안해서 그럼
        source_code1 = content1.get_attribute("outerHTML")
        driver.quit
        return source_code1
        
    def getTime(self):
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(self.url_)

        # xpath1 : '최적' 시간
        #xpath1 = '//*[@id="main_pack"]/section[1]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/ul/li[1]/div/div[1]/button[1]/dl/div[1]/dd/span/span[1]'
        #content1 = driver.find_element("xpath", xpath1)
        #content1_time = content1.text

        # xpath2 : '지하철' 시간
        # xpath2_1 = '//*[@id="main_pack"]/section[1]/div/div/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div/ul/li[3]/button'
        # time.sleep(3)
        # driver.find_element("xpath", xpath2_1).click() # "지하철" 버튼 클릭, 지하철 경로만 보이도록 함
        # xpath2_2 = '//*[@id="main_pack"]/section[1]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/ul/li[1]/div/div[1]/button[1]/dl/div[1]/dd/span/span[1]'
        # content2 = driver.find_element("xpath", xpath2_2)
        # content2_time = content2 #.text
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
    print(try1.UseSubway())
    # print(try1.getTime(1, 2))