''' Roll the dice '''

import random

def diceroll(): 
    num = random.randint(1,6)
    print(num)

print("Let's roll the dice!")
diceroll()
while True:
    ask = input("Would you like to roll the dice again?: ")
    if ask == "yes":
        diceroll()
    if ask == "no":
        print("Thank you and enjoy your day.")
        break
