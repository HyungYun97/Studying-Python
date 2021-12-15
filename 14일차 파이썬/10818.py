N = int(input()) # N은 주어지는 N개의 정수
numbers = list(map(int, input().split())) # numbers는 N개의 정수를 공백으로 구분해서 주어주는 수
a = numbers[0] # a라는 변수에 numbers 배열의 첫번째 수를 저장해준다. a 는 max 최대값을 저장해줄것이다.
b = numbers[0] # b라는 변수에 numbers 배열의 첫번째 수를 저장해준다. b는 min 최소값을 저장해줄것이다.

for i in numbers[1:]: # for문을 통해 i에 numbers의 값이 하나씩 저장된다.
    if a > i: 
        a = i # 최대값을 구하는 과정
    elif b < i:
        b = i # 최소값을 구하는 과정  
print(a,b) #마지막 print문은 들여쓰기된 문장들에서 나와 최종 결과만 출력할 수 있도록 설정해준다.