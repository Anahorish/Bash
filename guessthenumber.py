''' A number guessing game '''

import random

num = random.randint(1,100)
score = 100

while True:
    try:
        guess = int(input("Guess the number!: "))
        break
    except ValueError:
        print("That's not a number!")
        
while num != guess and score != 0:
    if guess < num:
        guess = int(input("Try a higher number!: "))
        score -= 10
        if guess > num:
            guess = int(input("That's too high: "))
            score -= 10
    if guess > num:
        guess = int(input("Try a lower number!: "))
        score -= 10
        if guess < num:
            guess = int(input("That's too low: "))
            score -= 10
    if guess == num:
        print("You guessed the right number!")
        print("This is your score:", score)
    
if score == 0:
    print("Game over! Please try again.")
