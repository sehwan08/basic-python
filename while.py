# customer = "Thor"
# index = 5

# while index >= 1:
#     print("{0}, here is your coffee!".format(customer))
#     print("We will throw it away if you do not come here in {0}".format(index))
#     index -= 1
#     if index == 0:
#         print("Ok your coffee is gone")

customer = "Thor"
person = "Unkown"

while person != customer :
    print("{0}, here is your coffee!".format(customer))
    person = input("Your name?: ->")
    if (person == customer):
        print("You can take this coffee")
    else:
        print("You are not Thor. Go away!")