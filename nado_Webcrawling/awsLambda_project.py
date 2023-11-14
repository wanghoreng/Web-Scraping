# [오늘의 날씨]
'''
흐림, 어제보다 OO°C 높아요.
현재 OO°C (최저 OO° / 최고 OO°)
오전 강수확률 OO% / 오후 강수확률 OO%

미세먼지 OO 좋음
초미세먼지 OO 좋음 
'''

import requests
import re
from bs4 import BeautifulSoup
import json


# 카카오톡 Access 토큰 => 12시간 마다 만료
KAKAO_TOKEN = "qhWB_b4tp69tjD2P2Ow803VnDVjGL5tAHzUKKiWQAAABi84Np9D-oZq-Jypvmw"

# 카카오톡 API 를 통해 전송하는 함수 
def sendTo_Kakao(text) :
  headers = {"Authorization":"Bearer " + KAKAO_TOKEN}
  url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
  post = {
    "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title": "바로 확인"
  }

  data = {"template_object": json.dumps(post)}
  return requests.post(url, headers=headers, data=data)


# bs4 를 통해 데이터 가져오는 함수 
def create_soup(url) : 

  headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

  try:
    res = requests.get(url, headers=headers)
    res.raise_for_status()  # HTTPError 발생 가능
    soup = BeautifulSoup(res.text, "lxml")
    return soup
  except requests.exceptions.RequestException as e:
      print("Error occurred: ", e)
      sendTo_Kakao("에러가 발생하였습니다. 확인해주세요.")


# 날씨정보 가져오는 함수 
def scrape_weather() : 
  weather_text = ""
  weather_text += "[오늘의 날씨]\n"
  url = "https://weather.naver.com/today/09545101?cpName=KMA"
  soup = create_soup(url)
  
  # 흐림, 어제보다 OO°C 높아요. 
  cast = soup.find("p", attrs={"class" : "summary"}).get_text().split()
  #현재 OO°C (최저 OO° / 최고 OO°) 
  curr_temp = soup.find("strong", attrs={"class":"current"}).get_text().strip()  # 만약 태그를 가져올 때 해당 태그 안에 불필요한 데이터가 있다면, replace 를 써서 빈칸으로 바꿔주자.
  min_temp = soup.find("span", attrs={"class": "lowest"}).get_text().strip()
  max_temp = soup.find("span", attrs={"class": "highest"}).get_text().strip()
  # 오전 강수확률 OO% / 오후 강수확률 OO%
  rain_rate = soup.find_all("strong", attrs={"class":"inner_text"})
  morning_RR = rain_rate[0].get_text().split()
  afternoon_RR = rain_rate[1].get_text().split()


  # 출력 
  weather_text += f"{cast[0]} / {cast[1]} {cast[2]} {cast[3]}💡\n"
  weather_text += "{} ({} / {})\n".format(curr_temp, min_temp, max_temp)
  weather_text += f"{morning_RR[0]} {morning_RR[1]} | {afternoon_RR[0]} {afternoon_RR[1]}\n\n"

  
  pattern = "최고기온([0-9]+)"
  result = re.search(pattern, max_temp)
  match = int(result.group(1))
  if match >= 7 and match <= 13: 
    weather_text += "오늘은 맨투맨에 후리스닷!!🧥 편하게 가자고~!"
  elif match >= 1 and match <= 6 : 
    weather_text += "오늘은 패딩 안입으면 춥겠는디?? 🤧 감기 조심혀!!"
  elif match <= 0 :   
    weather_text += "진짜 오늘은 날씨 미쳤어!! 장갑🧤이랑 목도리🧣 꼭 챙겨!"
  else : 
    weather_text += "겨울아닌 날씨는 잘 챙겨입을 수 있지?? ㅎㅋㅋ 패션 챙기자~ 🐯"

  r = sendTo_Kakao(weather_text)
  print(r.text)



if __name__ == "__main__" : 
  scrape_weather() # 오늘의 날씨 정보 가져오기 