def sum_even_odd(numbers):
    """
    Calculates the sum of even and odd numbers in a given list.

    Args:
        numbers (list of int): The list of integers to process.

    Returns:
        tuple: A tuple containing two integers:
            - The sum of even numbers.
            - The sum of odd numbers.

    Example:
        >>> sum_even_odd([1, 2, 3, 4])
        (6, 4)
    """
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum

# AI-generated docstring (example from Copilot):
# """
# Returns the sum of even and odd numbers in the given list.
#
# Args:
#     numbers (list): List of integers._
if __name__ == "__main__":
    input_str = input("Enter a list of integers separated by spaces: ")
    input_list = [int(x) for x in input_str.strip().split()]
    even_sum, odd_sum = sum_even_odd(input_list)
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")

# Comparison:
# Manual docstring is more detailed, follows Google Style, and includes an example.
# AI-generated docstring is shorter and less detailed.