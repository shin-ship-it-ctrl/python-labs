#3. Write a program to check if the input number is a prime number.
number = input("Enter a number: ")
number = int(number)
is_prime = True

if number <= 0:
    is_prime = False
elif number == 1:
    is_prime = True
else:
    for i in range(2, number):
        if number % i == 0:
           is_prime = False
           break

if is_prime:
    print("Number ", str(number), "is a prime number.")

else:
    print("Number ", str(number), "is not a prime number.")





