input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for i in array:
        if number == i:
            return True
    return False


result = is_number_exist(3, input)
print(result)