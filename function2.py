from random import *

# print(random())
# print(random() * 10)
# print(int(random()*10))
# print(int(random()*10)+1) #0을 제외하고 1~10 랜덤 값

# print(int(random()*45) + 1) #45개의 로또 번호 생성 가능

# #random 함수를 더 쉽게 쓰는 방법
# print(randrange(1, 46))
# print(randint(1, 45))

day = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 "+str(day)+"일로 선정 되었습니다.")
