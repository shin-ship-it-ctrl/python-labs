#4. Printing the square of the first 20 numbers using the while loop.

count = 1
square = 0
while count < 21:
    square = count ** 2
    print("The square of " + str(count) + " is " + str(square) + ".")
    count += 1
