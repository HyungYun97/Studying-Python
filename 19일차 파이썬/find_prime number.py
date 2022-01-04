input = 20


def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1): # n부터 number + 1 값까지 반복
        for i in prime_list: # i를 prime_list에 반복하며 저장
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)