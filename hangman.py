''' Hangman in Python '''

#import words.txt
import random

with open('words.txt', 'r') as file:
    guess_round = 10
    guess_no = 1
    file = file.readlines()
    word = random.choice(file)
    print(word)
    print('_' * len(word))
    guess = input("Guess a letter!: ")
    while guess_round != 0 and word != guess:
        for x in word:
            if x == guess:
                print(x)
            else:
                print('X')
                guess_round -= 1
                guess_no += 1
        guess = input("Guess a letter!: ")
print("You guessed it!")
