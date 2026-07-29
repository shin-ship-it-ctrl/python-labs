'''
2. Write a Python program to sum two integers. However, if the sum is between 15 and 20 it
will return 20.
'''
num1=int(input("Please enter first number: "))
num2=int(input("Please enter second number: "))

total = num1 + num2
if (total >=15) and (total<= 20):
    total = 20
    print("Total is " + str(total))
else:
    print("Total is " + str(total))

