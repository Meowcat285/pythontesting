import os

clear = lambda: os.system('clear')

clear()

rate = int(input("What is the current USD to YEN conversion rate? "))

money = int(input("How much money do you want to convert (USD please) "))

converted = (money * rate)

print("That is " + str(converted) + " YEN")