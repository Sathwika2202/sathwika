def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

try:
    score_input = float(input("Enter the score: "))
    print("Grade:", grade(score_input))
except ValueError:
    print("Invalid input. Please enter a numeric value.")