#3. Finding the average of 5 numbers using the while loop.
count = 1
total = 0
while count < 6:
    number = int(input("Enter " + str(count) +  " number: "))
    total = total + number
    count +=1
average = total / 5
print("The average is: " + str(average))
