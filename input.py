# import sys

# print("A", "B", sep=", ", end="!")

# #로그 처리시 필요
# print("A", file=sys.stdout) #실제 표준 출력으로 찍힘
# print("A", file=sys.stderr) #실제 표준 에러로 찍힘

# #글자 정렬
# score = {"Math":0, "English":50, "Coding": 100}
# for subject, score in score.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")


# #대기 순번표
# for num in range(1, 21):
#     print("Number : "+str(num).zfill(3)) #.zfill = 3개 만큼의 공간을 0으로 처리 있으면 없는 자리만


# answer = input("Enter anything: -> ")
# print("You entered: " + answer )



#빈 자리는 빈공간, 오른쪽 정렬, 총 10자리 공간 확보
print("{0: > 10}".format(500))

#양수일때 +, 음수일때 -
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

#왼쪽 정렬, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

#3자리 마다 콤마 
print("{0:,}".format(10000000))

#3자리 마다 콤마, +- 부호 붙히기
print("{0:+,}".format(10000000))

#3자리 마다 콤마, +- 부호 붙히기, 자리수 확보, 빈자리 ^채우기
print("{0:^<+30,}".format(10000000))

#소수점 출력
print("{0:f}".format(5/3))
#소수점 특정 자리 출력
print("{0:.2f}".format(5/3))
