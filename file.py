# 파일 쓰기
# score_file = open("score.txt", "w", encoding="utf-8")
# print("Math: 0", file=score_file)
# print("English: 100", file=score_file)
# score_file.close()

# 파일 이어 쓰기
# score_file = open("score.txt", "a", encoding="utf-8") #이어 쓰기
# score_file.write("Korean: 70")
# score_file.write("\nCoding: 90")
# score_file.close()

# # 파일 읽어 오기
# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read()) # 전부 읽어 오기
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.readline()) # 줄별로 읽기
# print(score_file.readline(), end="") # 줄별로 읽기
# print(score_file.readline()) # 줄별로 읽기
# print(score_file.readline()) # 줄별로 읽기
# score_file.close()

# 몇줄인지 모를 때
# score_file = open("score.txt", "r", encoding="utf-8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

#리스트형식으로 읽기
score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()
