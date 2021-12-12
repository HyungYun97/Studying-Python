N, X = map(int,input().split())
A = list(map(int,input().split()))
for i in range(N):
    if A[i] < N:
        print(A[i], end=" ") # 인터넷 도움 받음 for if문까지는 생각했는데 세세한 문법 정리가 부족했음.
        # end="~~"를 해주게되면 줄 바꿈으로 넘어가지않고 이어서 진행하게 됨
