a = [] # a라는 변수에 배열을 지정해줌
for i in range(9):
    a.append(int(input()))
print(max(a))
print(a.index(max(a))+1) # index함수는 index(값)의 위치를 List 배열 내에서 몇번째에 있는지 찾아주는 변수이다.
