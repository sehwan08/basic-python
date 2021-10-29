cabinet = {3:"Kim", 100:"Park"}
print(cabinet)
print(cabinet[3])
print(cabinet.get(3)) #get으로 없는 것을 찾으면 none 리턴
print(cabinet.get(5, "Availabe"))
print(3 in cabinet) #키 유무 확인

cabinet2 = {"A":"Kim", "B":"Park"} #키와 밸류는 문자열/숫자형 다 가능
print(cabinet2)

cabinet2["C"] = "Cha" #키와 밸류 추가
print(cabinet2)

del cabinet2["A"] #딕셔너리 내용 삭제
print(cabinet2) 

print(cabinet.keys()) #키만 출력
print(cabinet.values()) #밸류만 출력
print(cabinet.items()) #키&밸류 모두 출력

cabinet.clear()
print(cabinet)