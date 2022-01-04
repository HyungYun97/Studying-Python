input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
        for i in array: # array의 길이만큼 for문 실행
            if number == i: # 비교 연산 1번 실행
                return True # N * 1 = N 만큼
        return False #만약 input이 4가먼저 3이 마지막일경우 for문을 다 돌아야지만 찾을수있음.


result = is_number_exist(3, input)
print(result)