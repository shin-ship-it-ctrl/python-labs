'''
9. Write a program to count the number of even and odd numbers in a series of numbers.
Sample numbers: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers: 5
Number of odd numbers: 4
'''

def exercise_9_count_even_odd():
    """Counts the number of even and odd numbers in a sample tuple."""
    print("--- Exercise 9: Counting Even and Odd Numbers ---")
    # Sample numbers provided in the prompt
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    # Initialize counters
    even_count = 0
    odd_count = 0

    for num in numbers:
        # Check for evenness using the modulus operator (%)
        if num % 2 == 0:
            even_count += 1
        # If not even, it must be odd (assuming only integers)
        else:
            odd_count += 1

    print(f"Sample numbers: {numbers}")
    print(f"Number of even numbers: {even_count}")
    print(f"Number of odd numbers: {odd_count}")


if __name__ == "__main__":
    exercise_9_count_even_odd()