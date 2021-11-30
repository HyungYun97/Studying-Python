A, B = map(int,input().split())
if A>B:
    print(">")
elif A<B:
    print("<")
else :
    print("==") 

    # 파이썬은 if 조건 : 
    #         elif 조건 :
    #         else : (else는 if와 elif를 제외한 나머지이므로 따로 조건을 주지 않는다)