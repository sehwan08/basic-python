# weather = "sunny"
# weather = input("How is the weather today? -> ")

# if weather == "rain" or weather == "snow":
#     print("You should take an umbrella")
# elif weather == "cloudy":
#     print("You should take a jacket")
# else:
#     print("The weather is truly fine!")

temp = int(input("what temperature is it today? -> "))

if 30 <= temp:
    print("It is so hot! Stay at home")
elif 20 <= temp and temp < 30:
    print("Not bad today! Up to you")
elif 0 <= temp < 10:
    print("too cold!")
else:
    print("I do not know where the hell we are")
