#5. Finding the sum of the 50 even numbers using the while loop

even = 0
count = 1
while count < 51:
    if count % 2 == 0:
        even = even + count
    count += 1

print("The sum of even numbers is " + str(even) + ".")