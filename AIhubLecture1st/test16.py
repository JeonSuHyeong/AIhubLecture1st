from bs4 import BeautifulSoup
from urllib import request

#https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnld=108

target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnld=108")
soup = BeautifulSoup(target, "html.parser")

for location in soup.select("location"):
    print("도시 : ", location.select_one("city").string)
    print("날씨 : ", location.select_one("wf").string)
    
    print("")