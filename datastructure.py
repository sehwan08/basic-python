# menu = {"Coffe","Milk","Juice"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)


from random import *
participate = range(1,21) 
participate = list(participate)
shuffle(participate)

winners = sample(participate, 4) #중복을 없애기 위해서 4명을 미리 뽑음

print("-- Winner! --")
print("Winner for chicken : {0}".format(winners[0]))
print("Winner for coffee: {0}".format(winners[1:]))
print("-- Congratulation --")