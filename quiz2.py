# from random import *

# check ="O"
# customer_time = randint(5, 50)
# available_time = randint(5, 15)
# count = 0




# for i in range(1, 51):
#     if available_time >= 5 and available_time <= 15:
#         print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(check, i, available_time))
#         count += 1
#     elif available_time > 15:
#         check = ""
#         print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(check, i, customer_time))

# print("총 탑승 승객 : {0}분".format(count))

from random import randint, randrange


cnt = 0 # 총 탑승 승객
for i in range(1, 51):
    time = randint(5, 51) #randrange 동일
    if 5 <= time <= 15: #5~15분 이내
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: #매칭 실패
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}분".format(cnt))