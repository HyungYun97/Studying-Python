t = int(input())
for i in range(t):
    A, B = map(int,input().split())
    print(f'Case #{i+1}: {A+B}') # print(f) <- f-string print 함수 안에 문자열을 사용할 때, 따옴표 앞에 f를 접두사로 사용하면 변수들 출력 가능