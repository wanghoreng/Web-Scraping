# [오늘의 날씨]
'''
흐림, 어제보다 OO°C 높아요.
현재 OO°C (최저 OO° / 최고 OO°)
오전 강수확률 OO% / 오후 강수확률 OO%

미세먼지 OO 좋음
초미세먼지 OO 좋음 
'''
import re
import requests
from bs4 import BeautifulSoup


# bs4 를 통해 데이터 가져오는 함수 
def create_soup(url) : 
  headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
  res = requests.get(url, headers=headers)
  res.raise_for_status()
  soup = BeautifulSoup(res.text, "lxml")
  return soup

# 뉴스들 타이틀 및 링크 출력 함수 
def print_news(index, title, link) :
  print(f"{index+1}. {title}")
  print(f"  📂 {link}")

# 이미지 확인 함수 
def img_find(news) : 
  a_idx = 0 
  img = news.find("img")
  if img : 
    a_idx = 1 # img 태그가 있으면 1번째 a 태그의 정보를 사용
  return a_idx

# 날씨정보 가져오는 함수 
def scrape_weather() : 
  print("[오늘의 날씨]")
  url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EC%9A%A9%EC%9D%B8%EC%8B%9C+%EA%B8%B0%ED%9D%A5%EA%B5%AC+%EA%B5%AC%EA%B0%88%EB%8F%99+%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&tqi=ig%2BwtwqVN8VssuOrpy0ssssss48-115725"
  soup = create_soup(url)
  
  # 흐림, 어제보다 OO°C 높아요. 
  cast = soup.find("p", attrs={"class" : "summary"}).get_text().split()
  # 현재 OO°C (최저 OO° / 최고 OO°) 
  curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().strip()  # 만약 태그를 가져올 때 해당 태그 안에 불필요한 데이터가 있다면, replace 를 써서 빈칸으로 바꿔주자.
  min_temp = soup.find("span", attrs={"class": "lowest"}).get_text().strip()
  max_temp = soup.find("span", attrs={"class": "highest"}).get_text().strip()
  # 오전 강수확률 OO% / 오후 강수확률 OO%
  rain_rate = soup.find_all("span", attrs={"class":"weather_inner"})

  # 미세먼지 
  dust1 = soup.find_all("li",attrs={"class":"item_today level1"})


  # 출력 
  print(f"{cast[0]} {cast[1]} {cast[2]}💡 ({cast[3]})")
  print("{} ({} / {})".format(curr_temp, min_temp, max_temp))
  print(f"강수확률 {rain_rate[0].get_text().strip()} / {rain_rate[1].get_text().strip()} ")
  print()
  print(f"{dust1[0].get_text().strip()}")
  print(f"{dust1[1].get_text().strip()}")
  print()



# 헤드라인 뉴스 정보 가져오는 함수
def scrape_headline_news() : 
  print("[헤드라인 뉴스]")
  url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101"
  soup = create_soup(url)
  new_list = soup.find("ul", attrs={"class":"sh_list"}).find_all("li",limit=3)

  for index,news in enumerate(new_list):
    a_idx = img_find(news)
    title = news.find_all("a")[a_idx].get_text()
    link = news.find_all("a")[a_idx]["href"]
    print_news(index, title, link)
  print()
  

# IT 뉴스 가져오는 함수
def scrape_it_news() : 
  print("[IT 뉴스]")
  url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
  soup = create_soup(url)
  news_list = soup.find("ul",attrs={"class":"type06_headline"}).find_all("li",limit=3)

  for index,news in enumerate(news_list) :
    a_idx = img_find(news) 
    a_tags = news.find_all("a")[a_idx]
    title = a_tags.get_text().strip()
    link = a_tags["href"]
    print_news(index, title, link)
  print()
    
# 영어 회화 가져오는 함수
def scrape_english() : 
  print("[오늘의 영어 회화]")
  url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;"
  soup = create_soup(url)
  sentences = soup.find_all("div",attrs={"id":re.compile("^conv_kor_t")}) # conv_kor_t 로 시작하는 문자를 다 찾는 정규식표현
  print("🍊 영어지문")

  for sentence in sentences[len(sentences)//2:] : 
    print(sentence.get_text().strip())

  print()

  print("🥭 한글지문")

  for sentence in sentences[:len(sentences)//2] : 
    print(sentence.get_text().strip())
  
  



if __name__ == "__main__" : 
  scrape_weather() # 오늘의 날씨 정보 가져오기 
  scrape_headline_news() # 헤드라인 뉴스 가져오기
  scrape_it_news() # IT 뉴스 가져오기
  scrape_english() # 영어 회화 지문 가져오기
