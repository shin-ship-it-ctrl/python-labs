'''
6. Create a program that allows the user to guess a secret number between 1 and 100. The
program should keep prompting the user until they guess the correct number.
'''
import random

number = random.randint(1, 20)
guesses = 0
count = 0
while guesses != number:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess == number:
        print("You guessed the secret number!")
        guesses =  guesses + number
    count += 1



print("You had " + str(count) + " number of guesses!")
print("The secret number was: " + str(guesses))
