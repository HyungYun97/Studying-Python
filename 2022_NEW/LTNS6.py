a,b,c = map(int,(input().split()))

if a == b and b == c:
    print(10000+(a*1000))
elif a == b: #elif -> 다른 조건 부여 
    print(1000+(a*100))
elif b == c:
    print(1000+(b*100))
elif a == c:
    print(1000+(c*100))
else: # 위의 4개의 경우 모두 아니면 그외의 경우에는 ? 
    print(max(a,b,c)*100)

