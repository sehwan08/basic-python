#with으로 간단 파일 쓰기
# with open("study.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("Studying hard!")

#with으로 간단 파일 읽기
with open("study.txt", "r", encoding="utf-8") as study_file:
     print(study_file.read())
    