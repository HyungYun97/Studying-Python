A = int(input())
B = int(input())
C = int(input())
D = str(A * B * C) #문자열로 받아서 문자열을 체크
for i in range(10): # 0 ~ 9 까지
    count = D.count(str(i))
    print(count)