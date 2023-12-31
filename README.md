# Web Scraping
Python 웹 스크래퍼를 활용한 날씨 정보 기반의 옷 종류를 추천해주는 알림 봇 🤖

<br>

## 개발 배경 🧶

옷 패션을 꽤나 신경쓰는 저는 매번 외출하기 전 날씨를 확인합니다. <br><br>
이러한 반복적인 작업을 자동화하여 매일 오전 7시마다 <br> 날씨의 최고기온, 최저기온 과 현재온도 및 강수확률 등 확인하여 카카오톡으로 메세지를 전송하는 알림 봇을 만들어보기로 결정하였습니다. <br><br>
그리고 추가적으로 최고기온에 맞춰 옷을 재밌게 추천해준다면, <br> 평범하던 일상에 재미를 불어넣어줄 수 있을것 같아서
사람을 걱정하며 옷의 종류를 추천해주는 알림 봇을 구현하게 되었습니다.

<br>

## 구현 기능 🌂
1. 맞춤형 데이터 웹 스크래핑 기능 구현 
2. `AWS Lambda`에서 `EventBridge 스케줄러`를 통해 `카카오 메세지 API` 로 웹 스크래핑 데이터 전송 기능 구현 

<br>

## 사용 기술 🧵
- **AWS Lambda**
- **EventBridge**
- **Kakao API**
- **BeautifulSoup4**
- **requests**

<br>

### 개선할 점 
- KAKAO API 토큰이 12시간마다 종료되는 문제 발생 -> 텔레그램 봇 API 적용할 예정
- 추가적인 웹 스크래핑 데이터를 보낼 예정

   



