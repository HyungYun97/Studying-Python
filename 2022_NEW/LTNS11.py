b = int(input()) # for문에 활용할 input 값

c = 'O' # 입력된 값이 O인지 X인지 확인 
d = 'X'

for i in range(b):
    a = list(input())# 'O', 'X'를 저장할 배열 
    cntO = 0 # 점수 더하기 for문이 돌때마다 cnt0이 초기화
    sum = 0 # 전체 합산 될 점수 마찬가지 초기화
    for j in a:
        if j == c:
            cntO += 1
        else:
            cntO = 0
        sum += cntO
    print(sum)