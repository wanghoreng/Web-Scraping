import requests

url = "https://lets-go-it.tistory.com/"

headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

# url 을 가져올 때, headers 에 user agent 를 넘겨주는 것이다. 
res = requests.get(url, headers=headers)

res.raise_for_status()

with open("wanghoreng.html","w", encoding="utf8") as f : 
  f.write(res.text)