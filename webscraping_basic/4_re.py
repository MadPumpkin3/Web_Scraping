# 정규식: 정해진 형태의 식
# 예1) 주민등록번호: 960617-1111111
# 예2) 이메일 주소: fpdjxpa37@gmail.com
# 예3) 차량번호: 123가 1234
# 예4) IP주소: 129.168.0.1

import re
# 예문1) 뺑소니 사고를 목격하였고, 나는 뺑소는 차량의 번호를 보았다.
# 예문2) 차량번호 형태는 문자열로 되어 있다(abcd, book, desk 등)
# 예문3) 나는 차량번호 4자리 중 3자리만 기억이 난다.(ca?e)

p = re.compile("ca.e")
# p = re.compile 진행 시 보통 p로 받아옴.
# compile : 컴퓨터 언어(기계어)로 변환하는 것
# . (점, ca.e): 하나의 문자를 의미 > care, cafe, case (o) | caffe(x)
# ^ (^de) : 문자열의 시작을 의미 > desk, destination (o) | fade(x)
# $ (se$) : 문자열의 끝을 의미 > case, base (o) | face (x)

def print_match(m):
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환 / 일치하지 않았을 경우 오류 반환
        print("m.string:", m.string) # 입력받은 문자열 반환
        print("m.start:", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print('매칭되지 않음')
        
# m = p.match("care") # match: 주어진 문자열의 처음부터 일치하는지 확인 (예, careless > 앞 4자리는 일치 = True)
# print_match(m)
# match(n) : 'p'에 들어있는 단어와 'n'이 비슷한지 확인하는 것

# m = p.search("good care") # search: 주어진 문자열 중에 일치하는게 있는지 확인 (예, good care > care이 포함되어 있음 = True)
# print_match(m)

# lst = p.findall("good care cafe") # findall:일치하는 모든 것을 리스트 형태로 반환
# print(lst)

# 정규식을 쓸 때
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . (점, ca.e): 하나의 문자를 의미 > care, cafe, case (o) | caffe(x)
# ^ (^de) : 문자열의 시작을 의미 > desk, destination (o) | fade(x)
# $ (se$) : 문자열의 끝을 의미 > case, base (o) | face (x)