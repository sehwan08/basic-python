# sentence = 'I am a boy'
# print(sentence)
# sentence2 = "Python is easy"
# print(sentence2)
# sentence3 = """
# I am a boy,
# python is easy
# """
# print(sentence3)

# jumin = "990120-1234567"
# print("성별: "+jumin[7])
# print("년도: "+jumin[0:2])
# print("월일: "+jumin[2:6])
# print("생년월일: "+jumin[:6])
# print("뒷 7자리: "+jumin[7:])
# print("뒷 7자리(뒤에서부터): "+jumin[-7:])

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("python","Java"))

# index = python.index("n")
# print(index)
# inedx = python.index("n", index+1) #','이후 또 "n"을 찾음
# print(index)

# print(python.find("Java")) #없는값을 -1로 돌려줌 

# print(python.count("n"))


# print("나는 %d살 입니다." % 20) #%d = 정수값만
# print("나는 %s을 좋아해요." % "파이썬") #%s = String값만, %s는 정수,문자하나 다 표현 가능
# print("Apple은 %c로 시작해요." % "A") #%c = 문자 하나만
# print("나는 %s색과 %s색을 좋아해요" %("파랑", "초록"))
# print("나는 {}살 입니다".format(20))
# print("나는 {}색과 {}색을 좋아해요" .format("파랑","초록"))
# print("나는 {0}색과 {1}색을 좋아해요" .format("파랑","초록"))
# print("나는 {1}색과 {0}색을 좋아해요" .format("파랑","초록"))
# print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="초록"))

# age = 20
# color = "초록"
# print(f"나는 {age}살이며, {color}색을 좋아해요")

# print("I am a boy.\nYou are a girl") #줄 바꿈
# print("I am '\Sehwan\'")
# print("I am \"Sehwan\"")
# print("C:\\devtools\\pythonworkspace")#경로시 \\(2개) 필요
# print("Red Apple\rPine")#'\r'부터 모든 글자의 위치를 맨 앞으로 변경
# print("Redd\bAppel") #'\b' 한글자 삭제
# print("Red\tApple") #'\t' 탭

url = "http://naver.com"
parse1 = url.replace("http://", "") #규칙1
parse1 = parse1[:5] #규칙2
parse2 = parse1[:3] #nav

final = parse2 + str(len(parse1)) + str(parse1.count("e")) + "!"
print("{0} 사이트의 비밀번호 : {1}".format(url,final))





