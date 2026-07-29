'''
9. Write a program that asks the user his/her year of birth and calculates his/her age. If he/she
is below 18 years old, the program must display “You are a child aged <age>!”. Otherwise,
it must display “You are an adult aged age years old!”. (Assume that the age is calculated
based on the year only)
Sample input:
Input your year of Birth: 2000
Output:
You are a child aged 24
Sample input:
Input your year of Birth: 1994
Output:
You are an adult aged 30
'''


print("Input your year of Birth: " , end="")
userDOB = int(input())


age = 2026 - userDOB

if age < 18:
    print("You are a child aged " + str(age) + " years old!")
else:
    print("You are an adult aged " + str(age)  + " years old!")
