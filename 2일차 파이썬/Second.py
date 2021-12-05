#print 기초 2

print("Mary's cosmetic\n") # 작은 따옴표 '' 안에는 큰따옴표로 표시 "" \n 줄바꿈 표시 

print('신씨가 소리 질렀다. "도둑이야" \n') #큰따옴표 안에는 작은 따옴표로 표시

print("안녕하세요.\n만나\t\t반갑습니다.") # \n 줄바꿈 표시, \t 탭표시

print("오늘은", "일요일") # 여러값을 출력하기 위해 print 안에 쉼표로 구분이 가능하다.

print("naver","kakao","sk","samsung", sep=";") 

# naver/kakao/sk/samsung 출력

# sep는 출력문 사이에 해당하는 내용을 넣을 수 있음. 기본값은 공백
print("naver","kakao","sk","samsung", sep="/")

#줄바꿈 없이 출력 
#end="" print문을 이용해 출력을 완료한 뒤의 내용 수정 가능
print("first", end="");print("second")


#연산 결과 출력 5/3의 결과를 화면에 출력
# 출력하고 싶은 값을 print함수 인자에 적으면 되지만, 변수 a,b에 저장해서 적음
a = 5
b = 3
print(a/b)
