def solution(price, money, count):
    d = 0
    for i in range(count+1):
        d = price * i
        money = money - d
        if money < 0:
            answer = money * (-1)
            
            return answer

            #3 20 4 10