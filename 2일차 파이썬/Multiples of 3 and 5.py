#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

sum=0 # 누적합을 저장할 변수 0으로 설정

for num in range(1000): # 1000까지 변수를 num에 저장해줌
    if num % 3 == 0 or num %5 ==0:
        print(num)
        sum+=num

    print(sum)