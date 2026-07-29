'''
1. Write a program that asks the user for a number. If the number is even print ‘Even’, else
print ‘Odd’.
'''
print("Please enter a number: ", end="")
number = int(input())

if number % 2 == 0:
    print("It is an even number.")
else:
    print("It is an odd number.")

