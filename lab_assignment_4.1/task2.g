def factorial(n):
    if n < 0:
        result = "Factorial is not defined for negative numbers."
        print(result)
        return result
    elif n == 0:
        print("The factorial of 0 is 1")
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print(f"The factorial of {n} is {fact}")
        return fact

# Example usage:
factorial(5)   # Output: The factorial of 5 is 120
factorial(0)   # Output: The factorial of 0 is 1
factorial(-3)  # Output: Factorial is not defined for negative numbers