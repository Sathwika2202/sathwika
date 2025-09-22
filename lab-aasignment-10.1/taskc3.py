def calculate_percentage(value, percent):
    """
    Calculate the percentage of a given value.

    Parameters:
        value (float or int): The base value.
        percent (float or int): The percentage to calculate.

    Returns:
        float: The calculated percentage of the value.
    """
    return value * percent / 100  # Calculate percentage

base_amount = 200  # The base value to calculate percentage from
percentage = 15    # The percentage to calculate

result = calculate_percentage(base_amount, percentage)
print(result)  # Output the result
