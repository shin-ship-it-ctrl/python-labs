'''
10. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
Note: Use 'continue' statement.
Expected Output : 0 1 2 4 5
'''

def exercise_10_continue_statement():
    """Prints numbers 0 to 6, skipping 3 and 6 using the 'continue' keyword."""
    print("--- Exercise 10: Using 'continue' to Skip Numbers ---")
    output = []
    # Loop runs for x = 0, 1, 2, 3, 4, 5, 6
    for x in range(7):
        # If x is 3 or 6, the 'continue' statement is executed.
        if x == 3 or x == 6:
            # 'continue' jumps immediately to the next iteration of the loop,
            # skipping the append line below.
            continue

        # This line only executes for numbers 0, 1, 2, 4, 5
        output.append(str(x))

    print("Expected Output:", " ".join(output))


if __name__ == "__main__":
    exercise_10_continue_statement()