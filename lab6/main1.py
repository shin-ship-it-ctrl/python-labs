#1. Write a program to print counting from 1 to 10.
def exercise_1_counting_to_ten():
    """Prints numbers from 1 to 10 using a simple for loop."""
    print("--- Exercise 1: Counting to 10 ---")
    print("Counting:")
    for i in range(1, 11):
        # The range function (1, 11) includes 1 and goes up to (but not including) 11.
        print(i, end=" ")
    print() # Newline for clean output

if __name__ == "__main__":
    exercise_1_counting_to_ten()