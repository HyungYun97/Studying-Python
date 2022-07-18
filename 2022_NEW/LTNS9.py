a = [] # 배열 생성
for i in range(10): #for문으로 9개까지 입력 가능하도록 설정
    b = int(input()) # input 받기
    b = b % 42
    a.append(b) # input 되는 값을 a list 에 저장한다.

#set 함수를 활용해 a리스트의 중복된 값을 제거함
a = set(a)
print(len(a)) # a 리스트 안의 갯수를 출력



# 파이썬 set 함수 = 중복된 값을 가질 수 없음

# for (변수명) in range(범위): ~~~ 