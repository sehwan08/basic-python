my_set = {1,2,3,3,3}
print(my_set)

java = {"Yoo", "Kim", "Yang"}
python = set(["Yoo", "Park"])

#교집합 - 둘다 가능
print(java & python)
print(java.intersection(python))

#합집합 - 둘중 하나라도 가능
print(java | python)
print(java.union(python))

#차집합 - 하나만 가능
print(java - python)
print(java.difference(python)) #자바객체에는 있고, 파이썬에는 없는 값

#집합에 추가
python.add("Kim")
print(python)

#집합에 삭제
java.remove("Yang")
print(java)