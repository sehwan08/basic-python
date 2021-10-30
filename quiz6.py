class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1

while(True):
    try:
        print("Left chicken : {0}".format(chicken))
        order = int(input("How many chickens do you want -> "))
        if order > chicken:
            print("No more chickens")
        elif order <= 0:
            raise ValueError
        else:
            print("Waiting number [{0}]. {1} chicken(s) ordered.".format(waiting,order))
            waiting += 1
            chicken -= order
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("Wrong order")
    except SoldOutError:
        print("No more chickens")
        break
