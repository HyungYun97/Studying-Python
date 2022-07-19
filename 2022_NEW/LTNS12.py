a = int(input()) # 첫번째 for문을 돌릴 test case

for i in range(a):
    new_list = list(map(int,input().split()))
    avg = sum(new_list[1:])/new_list[0] # 평균을 구한다 전체 점수 / 학생수

    cnt = 0
    for j in new_list[1:]: # new_list[0] : 각 테스트 케이스의 개수 
        if j > avg:
            cnt += 1
        high_avg = (cnt/new_list[0]) * 100 # 비율 -> 평균이상수 / 전체학생수 * 100

    print('{0:0.3f}'.format(high_avg))
    # format 함수 사용 정수형은 {인자:0Nd} -> N 표현할 자리수
    # 실수형은 {인자:0.Nf} -> 마찬가지 N 소수점 아래 자리수

    # list 함수는 range 함수에 포함되지 않고 단독적으로 사용된다.
