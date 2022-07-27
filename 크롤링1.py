# https://blog.naver.com/nkj2001/222687225166
# 크롤링에 사용되는 urllib.request import
import urllib.request
# 웹페이지를 request 객체로 생성
request = urllib.request.Request('https://naver.com')
# 객체의 웹페이지에 이제 접속
response = urllib.request.urlopen(request)
# 서버의 응답을 read()를 통해 받아옴
# 이때 받아온 데이터는 문자열이 아닌 byte이므로 decode()함수로 utf-8로 변경
htmlBytes = response.read()
htmlStr = htmlBytes.decode("utf-8")
# print(htmlStr)
htmlSplit = htmlStr.split('\n')
for line in htmlSplit:
    print(line)