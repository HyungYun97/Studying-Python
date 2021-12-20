def solution(price, money, count):
    
    d = 0
    
    for i in range(count+1):
        
        d += price * i
        
        
    if money > d:
        return 0
    else:
        return d - money