'''
7. Write a Python program to guess a number between 1 and 9.
Note: The user is prompted to enter a guess. If the user guesses wrong then the prompt
appears again until the guess is correct, on successful guess, the user will get a "Well
guessed!" message, and the program will exit.
'''
import random

number = random.randint(1, 9)
i = int(input("Guess a number between 1 and 9: "))
if i != number:
    print("You guessed the wrong number!")
    exit()
else:
    print("Well guessed!")

