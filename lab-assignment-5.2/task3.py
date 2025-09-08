# Function to calculate the nth Fibonacci number using recursion
def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    # Base cases: 0th Fibonacci is 0, 1st Fibonacci is 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: sum of previous two Fibonacci numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
if __name__ == "__main__":
    n = 6  # Change this value to compute a different Fibonacci number
    print(f"The {n}th Fibonacci number is {fibonacci(n)}")

"""
Explanation:
-------------
- The function 'fibonacci' computes the nth Fibonacci number using recursion.
- It checks for base cases (n == 0 or n == 1) and returns the corresponding value.
- For other values, it recursively calls itself to compute the sum of the previous two Fibonacci numbers.
- The function raises a ValueError if the input is negative.
- The example usage demonstrates how to call the function and print the result.
"""