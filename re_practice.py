import re # 정규식을 할 때 사용하는 라이브러리 

# compile 함수 : 문자열을 컴파일하여 파이썬 코드로 변환한다. 
p = re.compile("ca.e") 
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de) : 문자열의 시작 > desk, deny (O) | fade(X)
# $ (se$) : 문자열의 끝 > case, base(O) | face(X)


def print_match(m) : 
  if m : 
    print("m.group() :",m.group()) # 매치객체.group() : 매치가 되면 매치된 값을 반환, 아니면 에러발생 
    print("m.string :",m.string) # 입력받은 문자열 반환
    print("m.start() :",m.start()) # 일치하는 문자열의 시작 index
    print("m.end() :",m.end()) # 일치하는 문자열의 끝 index
    print("m.span() :",m.span()) # 일치하는 문자열의 시작 /끝 xindex
  else : 
    print("매칭되지 않음")


# match 함수 : 문자열의 시작부분부터 패턴과 매칭이 되는지 검사한다. 
# m = p.match("caffe") 
# print_match(m)

# search 함수 : 주어진 문자열 중에 일치하는게 있는 지확인 
m = p.search("good care")
print_match(m)
'''
m.group() : care
m.string : good care
m.start() : 5
m.end() : 9
m.span() : (5, 9)
'''

# findall 함수 : 일치하는 모든 것을 리스트 형태로 반환 
lst = p.findall("good care cafe") 
print(lst)
# ['care', 'cafe']