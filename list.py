subway = [10, 20, 30]
print(subway)

subway2 = ["Lee", "Kim", "Cha"]
print(subway2)

print(subway2.index("Kim")) 

subway2.append("Park") #그냥 추가
print(subway2)

subway2.insert(1, "Jung")#원하는 위치에 추가
print(subway2)

print(subway2.pop()) #뒤에서부터 하나씩 제거
print(subway2)

subway2.append("Kim")
print(subway2.count("Kim")) #카운트

num_list = [5,6,1,2,9]
num_list.sort() #차례대로 정렬
print(num_list)
num_list.reverse()
print(num_list) #큰거부터 정렬
num_list.clear()
print(num_list) #리스트 내용 다 지우기

#파이썬에서는 리스트에 자료형 다 사용 가능
num_list = [5,6,1,2,9]
mix_list = ["조세호", 20, True]
print(mix_list)

num_list.extend(mix_list)
print(num_list)



