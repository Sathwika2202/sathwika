# Corrected and explained code:

# Calculate average score of a student
def calc_average(marks):
    total = 0
    for m in marks:
        total += m
    average = total / len(marks)
    return average   # Fixed typo: 'avrage' -> 'average'

marks = [85, 90, 78, 92]
print("Average Score is", calc_average(marks))  # Added missing parenthesis

# Explanations of the fixes:
# 1. Fixed the typo in the return statement: changed 'avrage' to 'average'.
# 2. Added the missing closing parenthesis in the print statement.
