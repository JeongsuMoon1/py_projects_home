'''
연속데이터( 시퀀스타입 )
> 튜플: () -> 
수정불가 -> immutable 
값을 묶는다!!(관계없는 데이터들을), 순서가 있다, 정방향/역방향(사용된적은 없지만 확인이 필요)
=> 함수에서 여러값을 리턴할 때 => 튜플로 적용되서 리턴 된다
맴버가 1개이면 => (1, ) 만약 (1) <- 이것은 값1 소괄호
'''
tu = ()
print( tu, len(tu), type(tu) )
tu = tuple()
print( tu, len(tu), type(tu) )
# 인덱싱, 슬라이싱, 정방향, 역방향 모두 적용
# 수정할 수 없다, 다 묶어서 관리 -> 기본은 리스트로 관리
tu = (1,2,3,4)
print( tu[0] )
print( tu[:2] )
print( tu[-1] )
a = (5,6,7,8)
print( tu + a )
# 함수에서 튜플 형태 리턴값 및 변수에서 받아서 처리하는 부분 확인