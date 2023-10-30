# [오늘의 날씨]
'''
흐림, 어제보다 OO°C 높아요.
현재 OO°C (최저 OO° / 최고 OO°)
오전 강수확률 OO% / 오후 강수확률 OO%

미세먼지 OO 좋음
초미세먼지 OO 좋음 
'''

import requests
from bs4 import BeautifulSoup

def scrape_weather() : 
  print("[오늘의 날씨]")
  url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EC%9A%A9%EC%9D%B8%EC%8B%9C+%EA%B8%B0%ED%9D%A5%EA%B5%AC+%EA%B5%AC%EA%B0%88%EB%8F%99+%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&tqi=ig%2BwtwqVN8VssuOrpy0ssssss48-115725"
  res = requests.get(url)
  res.raise_for_status()
  soup = BeautifulSoup(res.text, "lxml")
  # 흐림, 어제보다 OO°C 높아요. 
  cast = soup.find("p", attrs={"class" : "summary"}).get_text().split()
  # 현재 OO°C (최저 OO° / 최고 OO°) 
  curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text()  # 만약 태그를 가져올 때 해당 태그 안에 불필요한 데이터가 있다면, replace 를 써서 빈칸으로 바꿔주자.
  min_temp = soup.find("span", attrs={"class": "lowest"}).get_text()
  max_temp = soup.find("span", attrs={"class": "highest"}).get_text()
  # 오전 강수확률 OO% / 오후 강수확률 OO%
  rain_rate = soup.find_all("span", attrs={"class":"weather_left"})

  # afternoon_rain_rate = soup.find("span", attrs={"class":"weather_inner"}).get_text() 

  # 출력 
  print(f" {cast[0]} {cast[1]} {cast[2]}💡 ({cast[3]})")
  print("{} ({} / {})".format(curr_temp, min_temp, max_temp))
  print(f" 강수확률 {rain_rate[0].get_text()} / {rain_rate[1].get_text()} ")



if __name__ == "__main__" : 
  scrape_weather() # 오늘의 날씨 정보 가져오기 
