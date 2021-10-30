# def open_account():
#     print("An account was just opened")


# def deposit(balance, money):
#     print("Deposit completed. Your balance :{0}".format(balance + money))
#     # return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("Withrdawl succeeded. Your balance : {0}".format(balance-money))
#     else:
#         print("Withrawal canceled. Your balance : {0}".format(balance))


# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# # # balance = 100
# # # deposit(balance, 2000)
# # balance = 0
# # balance = deposit(balance, 1000)
# # # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)

# balance = deposit(0, 1000)
# print(balance)
# # balance = 0
# # balance = deposit(balance, 1000)
# # commision, balance = withdraw_night(balance, 500)
# # print(commision, balance)

# def profile(name, age=17, main_lang="Python"):
#     print("Name:{0}\t Age:{1}\t Language:{2}" \
#         .format(name,age,main_lang))

# profile("Kim")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="Kim", main_lang="Python", age=18)
# profile(age=20, name="Vic", main_lang="C++")

def profile(name, age, *language):
    print("Name: {0} Age:{1}".format(name,age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("Kim", 22, "Python", "Java", "C", "C++", "C#")
profile("Vic", 33, "Kotlin", "Swift")
