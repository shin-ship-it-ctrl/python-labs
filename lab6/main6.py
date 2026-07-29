'''
6. Write a program to print all the numbers between 1000 and 2000 which are divisible
by 7 but are not a multiple of 5.
'''

def exercise_6_divisible_by_7_not_5():
    """Finds numbers between 1000 and 2000 (exclusive) divisible by 7 but not 5."""
    print("--- Exercise 6: Divisible by 7, NOT multiple of 5 (1000-2000) ---")
    result_numbers = []
    # Range is 1001 to 1999 for numbers *between* 1000 and 2000
    for num in range(1001, 2000):
        # Condition 1: Divisible by 7 (remainder is 0)
        is_divisible_by_7 = (num % 7 == 0)
        # Condition 2: Not a multiple of 5 (remainder is not 0)
        is_not_multiple_of_5 = (num % 5 != 0)

        if is_divisible_by_7 and is_not_multiple_of_5:
            result_numbers.append(str(num))

    # Print results, 10 numbers per line for readability
    print("Numbers found:")
    # Use a loop to chunk the list for printing
    for i in range(0, len(result_numbers), 10):
        print(" ".join(result_numbers[i:i + 10]))


if __name__ == "__main__":
    exercise_6_divisible_by_7_not_5()