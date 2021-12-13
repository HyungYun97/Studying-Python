while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break

    # try 와 except 를 활용하는 문제
    # try를 입력하고 조건을 주면 try에 맞는 조건이 출력된다. int 를 input 해줘야하기 때문에 정수가 아닌 다른 것을 넣어주게 되면 
    # except문이 발동돼서 자동으로 break가 걸린다.