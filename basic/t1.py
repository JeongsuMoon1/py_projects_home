# 문자열을 숫자(정수)로 변환이 가능한지 체크하는 내용
A = [
''
,'1'
,'1.1'
,'A'
,'a'
,'$'
,'가'
]
# is함수 : 판독함수(그렇냐, 아니냐)
for data in A:
    print( data,data.isalpha(), data.isdecimal(), data.isdigit(), data.isnumeric() ) 

# 외장함수 => 가져오는 절차 import가 반드시 같이 존재한다
# 모듈을 가지고와서 그안에 존재하는 함수를 사용하는 케이스
import random
for n in range(10):
    # 난수범위는 : 시작경계값 <= 난수 <= 끝경계값
    #print( random.randint(1,3) )
    print( random.randint(0,99) )