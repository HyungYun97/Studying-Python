

def solution(array, commands):
    answer = []
    
    # array=[1,5,2,6,3,7,4] 근데 0부터 시작하니까 0의 위치가 4로 옮겨져서 1이 1로 보여야함

    for i in commands:
        # i 라는 변수안에 i,j,k의 모델이 모두 들어가있음 그래서 0,1,2로 출력값을 표출하면됨
        ans_array = array[i[0]-1:i[1]]
        ans_array.sort()
        answer.append(ans_array[i[2]-1])
    
    # answer에 append함수 (추가하다), ans_array에서 오름차순으로 정의된 i[2]-0 번째 수를 넣어줘라
    
    return answer