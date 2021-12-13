while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(A+B)

    # 내 첫번째 풀이는 반복문 안에 response = print(A+B) 를 사용했다. 그렇게되면 반복문 내에서 응답된 값은 계속적으로 출력이 되고 0 0 을 입력해 break를 걸어줄 때 
    # 0 + 0 = 0 0도 같이 출력해버리는게 틀린 요소로 작용했다. 고로 break문 밖으로 print를 빼고 출력했더니 올바른 답이 되었다.