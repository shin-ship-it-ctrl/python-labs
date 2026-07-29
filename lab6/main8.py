'''
8. Write a program to calculate the factorial of a number.
'''


def exercise_8_calculate_factorial():
    """Calculates the factorial of a user-input number."""
    print("--- Exercise 8: Calculating Factorial ---")
    try:
        # Prompting for input is only supported in a terminal/console environment.
        num = int(input("Enter a non-negative integer to calculate its factorial: "))

        if num < 0:
            print("Factorial is not defined for negative numbers.")
            return
        elif num == 0:
            # Factorial of 0 is 1
            factorial = 1
        else:
            factorial = 1
            # Loop from 1 up to the number, multiplying factorial by each step
            for i in range(1, num + 1):
                factorial *= i

        print(f"The factorial of {num} is {factorial}")

    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")


if __name__ == "__main__":
    exercise_8_calculate_factorial()