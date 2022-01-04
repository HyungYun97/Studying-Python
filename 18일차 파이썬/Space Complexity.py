def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    max_occurrence = 0 # 1개의 공간 사용
    max_alphabet = alphabet_array[0] # 1개의 공간 사용

    for alphabet in alphabet_array:
        occurrence = 0 # 1개의 공간 사용
        for char in string:
            if char == alphabet:
                occurrence += 1

        if occurrence > max_occurrence:
            max_alphabet = alphabet
            max_occurrence = occurrence

    return max_alphabet

result = find_max_occurred_alphabet
print("정답 = a 현재 풀이 값 =", result("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", result("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", result("best of best sparta"))

# alphabet array -> 26개의 공간을 사용

# 총 29개의 공간 사용
def find_max_occurred_alphabet(string):
		alphabet_occurrence_list = [0] * 26 # -> 26 개의 공간을 사용합니다

for char in string:        # string 의 길이만큼 아래 연산이 실행
    if not char.isalpha(): # 비교 연산 1번 실행
        continue
        arr_index = ord(char) - ord('a')         # 대입 연산 1번 실행 
        alphabet_occurrence_list[arr_index] += 1 # 대입 연산 1번 실행 

    max_occurrence = 0      # 대입 연산 1번 실행 
    max_alphabet_index = 0  # 대입 연산 1번 실행 
    for index in range(len(alphabet_occurrence_list)):    # alphabet_array 의 길이(26)만큼 아래 연산이 실행
        alphabet_occurrence = alphabet_occurrence_list[index] # 대입 연산 1번 실행 
        if alphabet_occurrence > max_occurrence: # 비교 연산 1번 실행 
            max_occurrence = alphabet_occurrence # 대입 연산 1번 실행 
            max_alphabet_index = index           # 대입 연산 1번 실행 

    


result = find_max_occurred_alphabet
print("정답 = a 현재 풀이 값 =", result("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", result("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", result("best of best sparta"))


            #30개의 공간을 사용하지만 상수라 성능에 차이가 없다. 
            #시간 복잡도를 더 신경써야한다.
            #string의 길이는 N으로 표현하게된다. 연산은 + 비교연산, 대입연산
            # 26 * (1+2*N+3) = 52N+104 알파벳 배열수 * 대입연산 1번
            # 알파벳 배열 길이 * string 길이 * 연산횟수
            # 알파벳 배열 길이 * 연산횟수 (3번)

            # 두번째 시간 복잡도 계산
            # string의 길이 * 연산횟수 (3번)
            # 대입연산 2회 더하기
            # 알파벳 배열의 길이 * 연산횟수 (4번)
            # N*(1+2)+2+26*(1+3) = 3N + 106
            # N의 횟수를 가정하여 계산해보면 52N+104가 압도적으로 크다. 하지만, N^2이 훨씬 더 큼