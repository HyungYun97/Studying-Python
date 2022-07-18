from hashlib import new


n = int(input()) # 반복해서 출력할 횟수
a = list(map(int,input().split())) # 점수가 저장될 배열
M = max(a)
new = []

for i in range(n): # n횟수만큼 반복 출력
    new.append(a[i]/M*100)
print(sum(new)/len(a))

