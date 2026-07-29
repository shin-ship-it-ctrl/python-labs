'''
7. Write a Python program to find those numbers which are divisible by 7 and multiples
of 5, between 1500 and 2700 (both included).

'''

def exercise_7_divisible_by_7_and_5():
    """Finds numbers between 1500 and 2700 (inclusive) divisible by both 7 and 5."""
    print("--- Exercise 7: Divisible by 7 AND multiple of 5 (1500-2700) ---")
    result_numbers = []
    # Range includes both 1500 and 2700
    for num in range(1500, 2701):
        # Check if the number meets both conditions simultaneously
        if (num % 7 == 0) and (num % 5 == 0):
            result_numbers.append(str(num))

    print("Numbers found:")
    print(", ".join(result_numbers))

if __name__ == "__main__":
    exercise_7_divisible_by_7_and_5()