# A game where users attempt to guess a random number between 0 and 20
import random

correctNumber = random.randint(0,20)
numberOfAttempts = 1    #Takes at least 1 try

print('I am thinking of a number between 1 and 20.')

while True:
    print('Take a guess.')
    guess = int(input())

    if guess == correctNumber:
        print('Good job! You guessed my number in ' + str(numberOfAttempts) + ' guesses!')
        break
    elif guess < correctNumber:
        print('Your guess is too low.')
    else:
        print('Your guess is too high.')
    numberOfAttempts = numberOfAttempts + 1



