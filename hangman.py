''' Hangman in Python '''

#import words.txt
import random

with open('words.txt', 'r') as file:
    file = file.read()
    word = list(random.choice(file))
    guess = list(input("Guess a letter!: "))
    for x in guess:
        for y in word:
            if x == y:
                print(x)

