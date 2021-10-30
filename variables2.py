gun = 10

def checkpoint(soldiers):
    global gun #전역 공간에 있는 변수 사용시 'global'
    # gun = 20
    gun = gun - soldiers
    print("함수 내 남은 총 : {0}".format(gun))

def checkpoint_return(gun, soldiers):
    gun = gun - soldiers
    print("함수 내 남은 총 : {0}".format(gun))
    return gun


print("전체 총 수 : {0}".format(gun))
gun = checkpoint_return(gun, 2)
print("남은 총 수 : {0}".format(gun))