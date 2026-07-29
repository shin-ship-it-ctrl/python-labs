#4. Write a program to display all prime numbers within a range, e.g start range= 25, end range = 50

def exercise_4_primes_in_range(start_range=25, end_range=50):
    """Displays all prime numbers within a specified range."""
    print(f"--- Exercise 4: Primes within Range ({start_range} to {end_range}) ---")
    primes = []
    # Loop includes the end_range number
    for num in range(start_range, end_range + 1):
        if is_prime(num):
            primes.append(num)

    print(f"Prime numbers in the range are: {primes}")


if __name__ == "__main__":
    # Example usage with the specified range
    exercise_4_primes_in_range(start_range=25, end_range=50)




