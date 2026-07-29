'''
4. Write a program that allows you to input an integer value n. If n is greater than 100, it
displays the message ‘Wrong Input’, otherwise it displays all factors of n.
'''

n = int(input("Enter a number: "))

if n > 100:
    print("Wrong Input")
else:
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)



