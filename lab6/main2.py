#2. . Write a program that prompts the user to enter a given number and then prints all the divisors of the given number.

def exercise_2_find_divisors():
    """Prompts for a number and prints all of its positive divisors."""
    print("--- Exercise 2: Finding Divisors ---")
    try:
        # Prompting for input is only supported in a terminal/console environment.
        # Replace the input line with a fixed number if running in an environment
        # without interactive console access.
        num = int(input("Enter an integer to find its divisors: "))
        if num <= 0:
            print("Please enter a positive integer.")
            return

        divisors = []
        # Loop from 1 up to the number itself
        for i in range(1, num + 1):
            # A number 'i' is a divisor if the remainder of 'num / i' is 0
            if num % i == 0:
                divisors.append(i)

        print(f"The positive divisors of {num} are: {divisors}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    exercise_2_find_divisors()


