# try:
#     print("Only to devide")
#     nums = []
#     nums.append(int(input("Enter first number -> ")))
#     nums.append(int(input("Enter second number -> ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("That is not a correct input")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("an Error occured")


class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("Only one digit devide")
    num1 = int(input("Enter first number -> "))
    num2 = int(input("Enter second number -> "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("Wrong value. Only one digit")
except BigNumberError as err:
    print("An error occured. Only one Digit")
    print(err)
finally:
    print("Thanks for using this!")