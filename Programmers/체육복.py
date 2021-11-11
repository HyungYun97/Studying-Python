def solution(n, lost, reserve):
    answer = 0
    
    set_reserve = set(reserve)-set(lost) # set 자료형은 중복을 허용하지 않는 자료형이다. 집합별로 차집합을 수행해줌
    set_lost = set(lost) - set(reserve) #도난당한경우와, 체육복이 있는경우 중복될 수 있기때문에 전처리를 해주는 모습

    for i in set_reserve: #set_reserve에 저장된 배열을 i로 재정의 해주고
        if i-1 in set_lost:  # i-1, 왼쪽값을 우선적으로 set_lost값과 비교하게 된다.
            set_lost.remove(i-1) # 같은 값이 있다면 remove 를 이용해 지워주게 되고
        elif i+1 in set_lost: # i+1, 오른쪽 값을 탐색하여 마찬가지로 set_lost 값과 비교한다.
            set_lost.remove(i+1) # 그 뒤 오른쪽 값이 같다면 remove를 이용해 지워준다.
                
        answer = n-len(set_lost) #answer이라는 변수에 전체 n값에서 set_lost 변수의 개수만큼 빼줘서 값을 구한다.
        
    return answer

# 안되는 이유 answer이라는 변수에 이미 0 이라는 값을 설정해서 n-len(set_lost) 가 0인경우는 그냥 0이 출력된다.
# 그러므 answer 재정의해준것을 없애주고, 바로 n - len(set_lost)를 출력해주면 올바른 답이 나온다.

#다른사람의 코드 

# def solution(n, lost, reserve):
#     _reserve = [r for r in reserve if r not in lost]
#     _lost = [l for l in lost if l not in reserve]
#     for r in _reserve:
#         f = r - 1
#         b = r + 1
#         if f in _lost:
#             _lost.remove(f)
#         elif b in _lost:
#             _lost.remove(b)
#     return n - len(_lost)