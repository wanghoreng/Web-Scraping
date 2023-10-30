import requests
res = requests.get("https://www.google.com/")

print("status code : ", res.status_code) 
# 200 일 경우 정상 
# 403 일 경우 해당 페이지에 접근할 수 없다는 것을 말함

# 오류를 걸러내는 첫번째 방식 
if res.status_code == requests.codes.ok :  # 응답코드가 200일때와 같다는 표현식
  print("정상입니다.")
else : 
  print("문제가 생겼습니다. [에러코드", res.status_code,"]")

# 오류를 걸러내는 두번째 방식 
res.raise_for_status()
# 에러가 있다면 발생시키고 프로그램을 종료하고, 없다면 해당 표현식 아래 코드를 실행한다. 

# 링크에서 가져온 내용의 길이를 출력한다.
print(len(res.text)) 
print(res.text) # 이 내용을 파일로 확인해보자 

# 아래 문장을 살펴보면, 
'''
"mytistory.html" 이름으로 구성된 파일을 만들어, 쓰기 모드로 하고 utf-8 유니코드로 변환한다. 그 과정에서 만들어진 파일 변수를 f 로 하고 
파일안에 res.text 내용이 쓰여지게 해라.
'''
with open("mygoogle.html","w", encoding="utf8") as f : 
  f.write(res.text)