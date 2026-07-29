'''
5. Write a program that prints the numbers from 1 to 100. But for multiples of three print
“Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers
which are multiples of both three and five print “FizzBuzz”.
'''

def exercise_5_fizzbuzz():
    """Prints numbers 1 to 100, replacing multiples of 3 with 'Fizz',
    multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'."""
    print("--- Exercise 5: FizzBuzz (1 to 100) ---")
    results = []
    for i in range(1, 101):
        output = ""

        # Check for multiples of both 3 and 5 first (i.e., multiples of 15)
        if i % 3 == 0 and i % 5 == 0:
            output = "FizzBuzz"
        # Check for multiples of 3
        elif i % 3 == 0:
            output = "Fizz"
        # Check for multiples of 5
        elif i % 5 == 0:
            output = "Buzz"
        # Otherwise, the output is the number itself
        else:
            output = str(i)

        results.append(output)

    # Print the results in a comma-separated list
    print(", ".join(results))


if __name__ == "__main__":
    exercise_5_fizzbuzz()