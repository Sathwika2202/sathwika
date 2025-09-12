# Simple calculator script with basic arithmetic functions
def add(a, b):
    # Returns the sum of a and b
    return a + b

def subtract(a, b):
    # Returns the difference of a and b
    return a - b

def multiply(a, b):
    # Returns the product of a and b
    return a * b

def divide(a, b):
    # Returns the quotient of a divided by b
    # Handles division by zero
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Example usage
if __name__ == "__main__":
    x = 10
    y = 5
    print("Add:", add(x, y))         # Output: 15
    print("Subtract:", subtract(x, y)) # Output: 5
    print("Multiply:", multiply(x, y)) # Output: 50
    print("Divide:", divide(x, y))     # Output: 2.0

    """
Simple calculator script providing basic arithmetic functions: addition, subtraction, multiplication, and division.
Each function takes two numeric arguments and returns the result of the operation.
Division handles division by zero by returning an error message.
Includes example usage demonstrating each function.
"""