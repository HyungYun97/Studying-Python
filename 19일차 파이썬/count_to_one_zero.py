input = "011110"
# 011110
# 모두 0으로 만드는 방법에서 최소로 뒤집는 숫자
# count_to_all_zero
# 0 -> 1로 문자열이 전환되는 순간 count_to_all_zert +=
# 1) 뒤집어질때, 즉 0에서 1로 전환


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0
    if string[0] == '0':
        count_to_all_zero += 1
    else:
        count_to_all_one += 1
    for i in range(len(string) - 1):
        if string[i] != string[i+1]: # 1 ->0 , 0->1
            if string[i + 1] == '0':
                count_to_all_one += 1
            if string[i + 1] == '1':
                count_to_all_zero += 1

    return min(count_to_all_zero, count_to_all_one) #최소값 주는 함수


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)