input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
        for num in array:              # array 의 길이만큼 아래 연산이 실행
            for compare_num in array:  # array 의 길이만큼 아래 연산이 실행
                if num < compare_num:  # 비교 연산 1번 실행
                    break
        else:
            return max_num

        # 이중 for문일수록 시간복잡도가 배로 걸린다

def find_max_num(array):
    max_num = array[0]        
    for num in array:      
        if num > max_num:  
            max_num = num
    return max_num

result = find_max_num(input)
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))

# for문이 하나 시간복잡도와 연산이 간단해짐