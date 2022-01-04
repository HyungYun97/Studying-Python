input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    plus = 0
    for number in array:
        if number <= 1 or plus <= 1:
            plus += number
        else:
            plus *= number
    return plus


result = find_max_plus_or_multiply(input)
print(result)