A,B = map(int, (input().split())) #A,B -> 시간과 분
C = int(input()) # A는 입력되는 추가 값

A += int(C/60)
B += C%60

if B >= 60:
    A+=1
    B-=60

if A >= 24:
    A-=24

print(A,B) #if 문을 빠져나와서 최종 값만 출력 가능하게 설계